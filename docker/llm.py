from abc import abstractmethod
from enum import Enum

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
    
class ModelType(Enum):
    T5_TINY = "t5-tiny"
    TINY = "tiny"

def get_model(model_name: ModelType) -> LLM:
    if model_name == ModelType.T5_TINY:
        from docker.llms.t5tiny import T5TINY
        return T5TINY()
    
    elif model_name == ModelType.TINY:
        from docker.llms.tiny import TINY
        return TINY()
    else:
        raise ValueError(f"Model {model_name} not found. Please check the model name.")
