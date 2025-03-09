import os
import urllib.request as request
from zipfile import ZipFile
from src.text_summarizer.logging import logging
from src.text_summarizer.entity import DataIngestionConfig

## Component
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        local_dir = os.path.dirname(self.config.local_data_file)  # Extract parent directory
        os.makedirs(local_dir, exist_ok=True)  # Ensure directory exists

        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logging.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logging.info("File already exists")

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)  # Ensure directory exists

        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logging.info(f"Extracted {self.config.local_data_file} to {unzip_path}")


