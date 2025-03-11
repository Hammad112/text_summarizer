from src.text_summarizer.logging import logging
from src.text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage_2_data_transformation import DataTransformationTrainingPipeline

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


## Data Transformatikon

STAGE_NAME = "Data Transformation stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    data_transformation_training_pipeline = DataTransformationTrainingPipeline()
    data_transformation_training_pipeline.initiate_data_transformation()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e
