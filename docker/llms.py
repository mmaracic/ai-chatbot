from abc import abstractmethod

#https://huggingface.co/openai-community/gpt2
#tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#model = GPT2LMHeadModel.from_pretrained('gpt2')

#https://huggingface.co/microsoft/phi-1_5

class LLM:
    @abstractmethod
    def load_model(self):
        pass
    
    @abstractmethod
    def query_model(self, prompt: str):
        pass
    

def get_model(model_name: str) -> LLM:
    if model_name == "t5-tiny":
        from docker.llms.t5tiny import T5TINY
        return T5TINY()
    
    elif model_name == "tiny":
        from docker.llms.tiny import TINY
        return TINY()
