## Data Ingestion
from src.text_summarizer.constants import *
from src.text_summarizer.utils.common import read_yaml, create_directories
from src.text_summarizer.entity import DataIngestionConfig

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