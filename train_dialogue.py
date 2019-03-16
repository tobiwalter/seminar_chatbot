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
from rasa_core.policies.keras_policy import KerasPolicy, FormPolicy, EmbeddingPolicy, FallbackPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer, FullDialogueTrackerFeaturizer, 
LabelTokenizerSingleStateFeaturizer
# from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter

# Function

def train_dialog(dialog_training_data_file, domain_file, path_to_model = 'models\current\dialogue\embedding3'):
    logging.basicConfig(level= 'INFO')
    agent = Agent(domain_file, policies = [EmbeddingPolicy(rnn_size = 128,
    																											attn_shift_range = 10,
    																											 embed_dim = 100,
    																											  mu_pos = 0.7), 
    																			FallbackPolicy, FormPolicy])
    																	
    training_data = agent.load_data(dialog_training_data_file)
    agent.train(
            training_data,
            augmentation_factor=0,
            epochs=2000,
            batch_size=[8,64],
            validation_split=0.2,
            random_seed = 42)
    agent.persist(path_to_model)

# Train

train_dialog('stories', 'domain.yml')

# Loading the Agent
# rasaNLU = RasaNLUInterpreter("models\current\nlu_tf\default\seminarnlu")
# agent = Agent.load("models/current/dialogue/keras", interpreter = rasaNLU)
