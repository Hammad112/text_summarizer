from src.text_summarizer.components.data_transforamtion import DataTransformation
from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.logging import logging


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        logging.info("Starting Data Transformation")
        config=ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
        logging.info("Data Transfromation completed")
    
