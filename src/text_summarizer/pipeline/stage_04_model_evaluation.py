from src.text_summarizer.components.model_evaluation import ModelEvaluation
from src.text_summarizer.config.configuration import ConfigurationManager
from src.text_summarizer.logging import logging



class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        logging.info("Starting Model Evaluation")
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation_config=ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()
        logging.info("Model Evaluation Completed")



    
