from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from builtins import str
from flask import Blueprint, request, jsonify

from rasa_core.channels.channel import UserMessage, OutputChannel
from rasa_core.channels import RestInput

logger =logging.getLogger(__name__)

class SlackBot(OutputChannel):
  def __init__(self, slack_verification_token, channel):
    self.slack_verification_token = slack_verification_token
    self.channel = channel

  def send_text_message(self, recipient_id, message):
    from slackclient import SlackClient
    text = message
    recipient = recipient_id

    CLIENT = SlackClient(self.slack_verification_token)
    CLIENT.api_call('chat.postMessage', channel = self.channel, text =text, as_user = True)

  def send_attachment(self, recipient_id, attachment, message=""):
        recipient = self.slack_channel or recipient_id
        return super(SlackBot, self).api_call("chat.postMessage",
                                              channel=recipient,
                                              as_user=True,
                                              text=message,
                                              attachments=attachment)

  @staticmethod
  def _convert_to_slack_buttons(buttons):
      return [{"text": b['title'],
               "name": b['payload'],
               "type": "button"} for b in buttons]

  def send_text_with_buttons(self, recipient_id, message, buttons, **kwargs):
      recipient = self.slack_channel or recipient_id

      if len(buttons) > 5:
          logger.warning("Slack API currently allows only up to 5 buttons. "
                         "If you add more, all will be ignored.")
          return self.send_text_message(recipient, message)

      button_attachment = [{"fallback": message,
                            "callback_id": message.replace(' ', '_')[:20],
                            "actions": self._convert_to_slack_buttons(
                                buttons)}]

      super(SlackBot, self).api_call("chat.postMessage",
                                     channel=recipient,
                                     as_user=True,
                                     text=message,
                                     attachments=button_attachment)

class SlackInput(RestInput):

  @classmethod
  def name(cls):
        return "slack"

  @classmethod
  def from_credentials(cls, credentials):
        if not credentials:
            cls.raise_missing_credentials_exception()

        return cls(credentials.get("slack_token"),
                   credentials.get("slack_channel"))

  def __init__(self, slack_dev_token, slack_verification_token, slack_client, debug_mode):
    self.slack_dev_token = slack_dev_token
    self.debug_mode =debug_mode
    self.slack_client=slack_client
    self.slack_verification_token=slack_verification_token

    @staticmethod
    def _is_user_message(slack_event):
        return (slack_event.get('event') and
                (slack_event.get('event').get('type') == u'message' or
                 slack_event.get('event').get('type') == u'app_mention') and
                slack_event.get('event').get('text') and not
                slack_event.get('event').get('bot_id'))

    @staticmethod
    def _is_button_reply(slack_event):
        return (slack_event.get('payload') and
                slack_event['payload'][0] and
                'name' in slack_event['payload'][0])

    @staticmethod
    def _get_button_reply(slack_event):
        return json.loads(slack_event['payload'][0])['actions'][0]['name']

    @staticmethod
    def _sanitize_user_message(text, uids_to_remove):
        """Remove superfluous/wrong/problematic tokens from a message.
        Probably a good starting point for pre-formatting of user-provided text,
        to make NLU's life easier in case they go funky to the power of extreme.
        In the current state will just drop self-mentions of bot itself
        Args:
            text: raw message as sent from slack
            uids_to_remove: a list of user ids to remove from the content
        Returns:
            str: parsed and cleaned version of the input text
        """
        for uid_to_remove in uids_to_remove:
            # heuristic to format majority cases OK
            # can be adjusted to taste later if needed,
            # but is a good first approximation
            for regex, replacement in [(r'<@{}>\s'.format(uid_to_remove), ''),
                                       (r'\s<@{}>'.format(uid_to_remove), ''),
                                       # a bit arbitrary but probably OK
                                       (r'<@{}>'.format(uid_to_remove), ' ')]:
                text = re.sub(regex, replacement, text)

        return text.rstrip().lstrip()  # drop extra spaces at beginning and end

    def process_message(self, on_new_message, text, sender_id):
        """Slack retry to post messages up to 3 times based on
        failure conditions defined here:
        https://api.slack.com/events-api#failure_conditions
        """
        retry_reason = request.headers.environ.get('HTTP_X_SLACK_RETRY_REASON')
        retry_count = request.headers.environ.get('HTTP_X_SLACK_RETRY_NUM')
        if retry_count and retry_reason in self.errors_ignore_retry:
            logger.warning("Received retry #{} request from slack"
                           " due to {}".format(retry_count, retry_reason))

            return Response(status=201, headers={'X-Slack-No-Retry': 1})

        try:
            out_channel = SlackBot(self.slack_token, self.slack_channel)
            user_msg = UserMessage(text, out_channel, sender_id,
                                   input_channel=self.name())
            on_new_message(user_msg)
        except Exception as e:
            logger.error("Exception when trying to handle "
                         "message.{0}".format(e))
            logger.error(str(e), exc_info=True)

        return make_response()

  def blueprint(self, on_new_message):
    from flask import Flask, request, Response
    slack_webhook = Blueprint('slack_webhook', __name__)

    @slack_webhook.route('/', methods =['GET'])
    def health():
      return jsonify({'status':'ok'})

    # @slack_webhook.route('/slack/events', methods =['POST'])
    @slack_webhook.route("/webhook", methods=['GET', 'POST'])
    # def event():
    #   if request.json.get('type')== 'url_verification':
    #     return request.json.get('challenge'), 200

    #   if request.json.get('token')==self.slack_client and request.json.get('type') == 'event_callback':
    #     data = request.json
    #     messaging_events = data.get('event')
    #     channel = messaging_events.get('channel')
    #     user = messaging_events.get('user')
    #     text = messaging_events.get('text')
    #     bot = messaging_events.get('bot_id')
    #     if bot == None:

    #       on_new_message(UserMessage(text,SlackBot(self.slack_verification_token, channel)))
    #     return Response(), 200    
    #   elif request.form:
    #     output = dict(request.form)
    #     if self._is_button_reply(output):
    #         sender_id = json.loads(output['payload'][0])['user']['id']
    #         return self.process_message(
    #             on_new_message,
    #             text=self._get_button_reply(output),
    #             sender_id=sender_id)
    #     return make_response()

    def webhook():
      request.get_data()
      if request.json:
          output = request.json
          if "challenge" in output:
              return make_response(output.get("challenge"), 200,
                                   {"content_type": "application/json"})
          elif self._is_user_message(output):
              return self.process_message(
                  on_new_message,
                  text=self._sanitize_user_message(
                      output['event']['text'],
                      output['authed_users']),
                  sender_id=output.get('event').get('user'))
      elif request.form:
          output = dict(request.form)
          if self._is_button_reply(output):
              sender_id = json.loads(output['payload'][0])['user']['id']
              return self.process_message(
                  on_new_message,
                  text=self._get_button_reply(output),
                  sender_id=sender_id)

      return make_response()

          
    return slack_webhook