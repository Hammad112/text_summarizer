import os
from src.text_summarizer.logging import logging
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk

from src.text_summarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    ## Convert example to feature
    def convert_examples_to_features(self, example_batch):
        ## Input token IDs
        input_encodings = self.tokenizer(
            example_batch['dialogue'], max_length=1024, truncation=True, padding="max_length"
        )

        ## Target token IDs (using text_target to avoid deprecation warning)
        target_encodings = self.tokenizer(
            text_target=example_batch['summary'], max_length=128, truncation=True, padding="max_length"
        )

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        ## Ensure dataset path exists
        if not os.path.exists(self.config.data_path):
            raise FileNotFoundError(f"Dataset path {self.config.data_path} not found. Ensure the dataset is correctly saved.")

        ## Load dataset
        dataset_samsum = load_from_disk(self.config.data_path)
        
        ## Convert examples to features
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)

        ## Ensure root directory exists before saving
        os.makedirs(self.config.root_dir, exist_ok=True)

        ## Save processed dataset
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))

