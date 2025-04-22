from transformers import Pipeline
from docker.llm import LLM

class T5TINY(LLM):
    
    pipe: Pipeline
    
    def load_model(self):
        from transformers import pipeline
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        tokenizer = AutoTokenizer.from_pretrained("google/t5-efficient-tiny-nl32")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/t5-efficient-tiny-nl32")

        pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    def query_model(self, prompt: str) -> str:
        response = pipe([prompt])
        response_text = response[0]["generated_text"]
        return f"{response_text}"
