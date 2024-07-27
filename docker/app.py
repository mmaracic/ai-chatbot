from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from huggingface_hub import login
import torch

token = Path('token').read_text().strip()
print("Hugginface token is:", token)
login(token=token)

# llama model - https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct
pipe = pipeline(
    "text-generation",
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto"    
)

print("Model started")

# We define the app
app = FastAPI()

# We define that we expect our input to be a string
class RequestModel(BaseModel):
    input: str

# Now we define that we accept post requests
# ->  In APIs, requests are made to ask the API to perform a certain task — in this case to analyze a piece of text. 
@app.post("/sentiment")
def get_response(request: RequestModel):
    # We get the input prompt
    prompt = request.input

    # We use the hf model to classify the prompt
    response = pipe([prompt], max_new_tokens=256)

    response_text = response[0]["generated_text"][-1]
    return f"{response_text}"
