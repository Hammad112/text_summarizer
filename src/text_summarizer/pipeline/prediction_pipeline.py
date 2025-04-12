from src.text_summarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer,pipeline

class predictionPipeline:
    def __init__(self):
        self.config=ConfigurationManager().get_model_evaluation_config()



    def predict(self,text):
        tokenizer=AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {
            "length_penalty": 0.8,  # ✅ correct
            "num_beams": 8,         # ✅ correct
            "max_length": 128
        }


        pipe=pipeline('summarization',model=self.config.model_path,tokenizer=tokenizer)

        print("Dialogue")
        print(text)

        output=pipe(text,**gen_kwargs)[0]['summary_text']

        print("\n Model Summar:")
        print(output)

        return output

