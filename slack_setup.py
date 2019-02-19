from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter

# load your trained agent
agent = Agent.load("models\current\dialogue\embedding", interpreter=RegexInterpreter())

input_channel = SlackInput(
    slack_token="xoxb-464508724117-540995397493-gmwJLQZBEkAcUvpSIJF5fV4J",
    # this is the `bot_user_o_auth_access_token`
    # slack_channel="YOUR_SLACK_CHANNEL"
    # the name of your channel to which the bot posts (optional)
)

# set serve_forever=True if you want to keep the server running
s = agent.handle_channels([input_channel], 5004, serve_forever=False)