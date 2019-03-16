from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
import rasa_core.run
from rasa_core.utils import EndpointConfig

logger = logging.getLogger(__name__)

# def train_dialogue(domain_file = 'domain.yml',
# 					# model_path = './models/current/dialogue',
# 					training_data_file = 'stories.md'):

# 	agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy()])

# 	agent.train(
# 				training_data_file,
# 				max_history = 3,
# 				epochs = 300,
# 				batch_size = 50,
# 				validation_split = 0.2,
# 				augmentation_factor = 50)

# 	agent.persist(model_path)
# 	return agent

# def run(dbug=False):
#     if dbug:
#         init_debug_logging()
#     interpreter = RasaNLUInterpreter('models/nlu/current')
#     from rasa_core.utils import EndpointConfig
#     action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
#     agent = Agent.load("models/current/dialogue", interpreter=interpreter,action_endpoint=action_endpoint)
#     rasa_core.run.serve_application(agent,channel='cmdline')

def run(serve_forever=True):

    nlu_interpreter = RasaNLUInterpreter(".\\models\\current\\\\nlu_tf\\default\\seminarnlu")
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('.\\models\\current\\dialogue\\embedding5', interpreter=nlu_interpreter, action_endpoint=action_endpoint)
    #rasa_core.run.serve_application(agent ,channel='cmdline')

    return agent

if __name__ == '__main__':
	run()
