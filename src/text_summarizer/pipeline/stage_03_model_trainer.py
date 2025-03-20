from src.text_summarizer.components.model_trainer import ModelTrainer
from src.text_summarizer.entity import ModelTrainerConfig
from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.logging import logging


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def intiate_model_trainer(self):
        logging.info("Starting Data Transformation")
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()  
        logging.info("Data Transfromation completed")
    
