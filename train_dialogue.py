# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:51:45 2019

@author: Tobias
"""

# Imports

#-----------

# rasa core

import logging
from rasa_core import training
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies import FormPolicy
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
# from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter

# Function

def train_dialog(dialog_training_data_file, domain_file, path_to_model = 'models/current/dialogue/keras'):
    logging.basicConfig(level= 'INFO')
    agent = Agent(domain_file, policies = [MemoizationPolicy(max_history=10), KerasPolicy(max_history=10), ])
    training_data = agent.load_data(dialog_training_data_file)
    agent.train(
            training_data,
            augmentation_factor=50,
            epochs=300,
            batch_size=20,
            validation_split=0.2)
    agent.persist(path_to_model)

# Train

train_dialog('stories.md', 'domain.yml')

# Loading the Agent
rasaNLU = RasaNLUInterpreter("models\current\nlu_tf\default\seminarnlu")
agent = Agent.load("models/current/dialogue/keras", interpreter = rasaNLU)
