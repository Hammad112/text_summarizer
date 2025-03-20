import os
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import DataCollatorForSeq2Seq, TrainingArguments, Trainer
from datasets import load_from_disk
from src.text_summarizer.entity import ModelTrainerConfig
from src.text_summarizer.logging import logging  # Use custom logger

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        logging.info(f"Using device: {device}")

        # Load tokenizer and model
        logging.info("Loading tokenizer and model...")
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        model_pegasus.to(device)
        logging.info("Model and tokenizer loaded successfully.")

        # Define Data Collator
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        # Load dataset
        logging.info(f"Loading dataset from {self.config.data_path}...")
        dataset_samsum = load_from_disk(self.config.data_path)
        logging.info("Dataset loaded successfully.")
        
        # Training Arguments
        logging.info("Setting up training arguments...")
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.eval_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            logging_dir=os.path.join(self.config.root_dir, "logs"),
        )
        logging.info("Training arguments set up successfully.")
        
        # Trainer
        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            processing_class=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum['train'],
            eval_dataset=dataset_samsum['validation']
        )
        logging.info("Trainer initialized.")

        # Start Training
        logging.info("Starting training...")
        trainer.train()
        logging.info("Training complete.")

        # Save Model and Tokenizer
        logging.info("Saving trained model and tokenizer...")
        model_save_path = os.path.join(self.config.root_dir, "pegasus-samsum-model")
        tokenizer_save_path = os.path.join(self.config.root_dir, "tokenizer")
        model_pegasus.save_pretrained(model_save_path)
        tokenizer.save_pretrained(tokenizer_save_path)
        logging.info(f"Model saved at {model_save_path}")
        logging.info(f"Tokenizer saved at {tokenizer_save_path}")