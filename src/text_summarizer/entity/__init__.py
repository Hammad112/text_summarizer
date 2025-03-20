from dataclasses import dataclass
from pathlib import Path


## Data Ingestion Config
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

## Data Transformatikon Config
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: str

## Model Trainer
@dataclass
class ModelTrainerConfig:
    ## Config yaml
    root_dir: Path
    data_path: Path
    model_ckpt: str
    ## params yaml
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: float
    logging_steps: int
    eval_strategy: str
    eval_steps: int
    save_steps: int
    gradient_accumulation_steps: int