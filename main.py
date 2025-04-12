from src.text_summarizer.logging import logging
from src.text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.text_summarizer.pipeline.stage_2_data_transformation import DataTransformationTrainingPipeline
from src.text_summarizer.pipeline.stage_03_model_trainer import ModelTrainerTrainingPipeline
from src.text_summarizer.pipeline.stage_04_model_evaluation import ModelEvaluationTrainingPipeline


logging.info("Logging has started")

STAGE_NAME = "Data Ingestion stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    # data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    # data_ingestion_training_pipeline.initiate_data_ingestion()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e


## Data Transformatikon

STAGE_NAME = "Data Transformation stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    # data_transformation_training_pipeline = DataTransformationTrainingPipeline()
    # data_transformation_training_pipeline.initiate_data_transformation()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)
    raise e

## Model Training

STAGE_NAME = "Model Training stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    # model_training_pipeline = ModelTrainerTrainingPipeline()
    # model_training_pipeline.intiate_model_trainer()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)

## Model Evaluation
STAGE_NAME = "Model Evaluation stage"
try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
    model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
    print(model_evaluation_pipeline)
    model_evaluation_pipeline.initiate_model_evaluation()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logging.exception(e)