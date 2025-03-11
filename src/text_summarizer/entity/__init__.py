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