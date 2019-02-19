from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig

nlu_interpreter =RasaNLUInterpreter('.\\models\\current\\nlu_tf\\current') #train rasa_nlu
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('.\\models\\current\\dialogue', interpreter = nlu_interpreter,action_endpoint = action_endpoint) #train rasa_core

input_channel = SlackInput( #'xoxp-464508724117-465710727574-540189494177-4f95904a55f64408089532920b798a80',
							'xoxb-464508724117-540995397493-gmwJLQZBEkAcUvpSIJF5fV4J')
							#'zj2xHJiOZ7OXbMhJZL5ijoHV',
							#True)

agent.handle_channels([input_channel], 5004, serve_forever=True)
