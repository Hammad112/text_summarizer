from src.text_summarizer.components.data_ingestion import DataIngestion
from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.logging import logging


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        logging.info("Starting Data Ingestion")
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

        logging.info("Data Ingestion completed")
    
