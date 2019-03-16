from rasa_nlu.training_data.loading import load_data
# from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config

def train_nlu(data, config_file, model_dir):
	training_data =load_data(data	)
	trainer = Trainer(config.load(config_file))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name="seminarnlu")

#execute only if running as main programm not as imported module within another program
if __name__ == '__main__':
		("data/nlu_data","config_tf.yml","models/current/nlu_tf")
