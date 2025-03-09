from src.text_summarizer.logging import logging
from src.text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


logging.info("Logging has started")

STAGE_NAME = "Data Ingestion stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.initiate_data_ingestion()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e