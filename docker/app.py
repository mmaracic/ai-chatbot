from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from huggingface_hub import login

from docker.llm import LLM, ModelType, get_model

token = Path('token').read_text().strip()
print("Hugginface token is:", token)
login(token=token)


# We define the app
app = FastAPI()
model:LLM = None

class RequestDto(BaseModel):
    input: str

@app.post("/request")
def get_response(request: RequestDto):
    if model is None:
        return "Model not loaded. Please load a model first."

    # We get the input prompt
    prompt = request.input
    return model.query_model(prompt)

class ModelDto(BaseModel):
    model_type: str

@app.post("/set_model")
def set_model(request: ModelDto):
    # We get the input model type
    model_type = ModelType(request.model_type)
    
    global model
    model = get_model(model_type)
    model.load_model()
    return f"model {model_type} loaded"