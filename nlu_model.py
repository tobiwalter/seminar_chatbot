from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter

def train_nlu(data, config, model_dir):
	training_data =load_data(data)
	trainer = Trainer(RasaNLUConfig(config))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name="seminarnlu")

#execute only if running as main programm not as imported module within another program
if __name__ == '__main__':
	train_nlu("data/training_data.json","config.json","models/current/nlu")
