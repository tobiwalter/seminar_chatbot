
from rasa_nlu.training_data.loading import load_data

data = load_data('data/nlu_data/training_data.json')
train, test = data.train_test_split()

train.persist('data/nlu_data/train_split')
test.persist('data/nlu_data/test_split')