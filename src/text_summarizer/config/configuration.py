## Data Ingestion
from src.text_summarizer.constants import *
from src.text_summarizer.utils.common import read_yaml, create_directories
from src.text_summarizer.entity import DataIngestionConfig,ModelTrainerConfig,ModelEvaluationConfig
from src.text_summarizer.entity import DataTransformationConfig

class ConfigurationManager:
    def __init__(self, config_filepath: str = CONFIG_PATH, params_filepath: str = PARAMS_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Create necessary directories
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])  # Ensure directory exists

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )


## DATA TRANSFORMATION
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])  # Ensure directory exists

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )

        return data_transformation_config

## MODEL TRAINER

    def get_model_trainer_config(self) -> ModelTrainerConfig:  # <-- Moved outside __init__
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])  # Ensure directory exists

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            num_train_epochs=params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            per_device_eval_batch_size=params.per_device_eval_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            eval_strategy=params.eval_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,    
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )

        return model_trainer_config

## Model Evaluation
    def get_model_evaluation_config(self)-> ModelEvaluationConfig:
        config=self.config.model_evaluation
        
        create_directories([config.root_dir])

        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path,
            metric_filename=config.metric_filename
        )
        return model_evaluation_config

