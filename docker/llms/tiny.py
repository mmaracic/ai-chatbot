from transformers import Pipeline
from docker.llm import LLM

class T5TINY(LLM):
    
    pipe: Pipeline
    
    def load_model(self):
        from transformers import pipeline
        from transformers import AutoTokenizer, AutoModelForCausalLM
        MODEL_NAME = "arnir0/Tiny-LLM"
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

        self.pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            device_map="auto"    
        )

    def query_model(self, prompt: str) -> str:
        response = self.pipe([prompt], max_new_tokens=256)

        response_text = response[0][0]["generated_text"]
        return f"{response_text}"
