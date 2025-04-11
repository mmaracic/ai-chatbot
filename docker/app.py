from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel, AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
import torch

token = Path('token').read_text().strip()
print("Hugginface token is:", token)
login(token=token)

#https://huggingface.co/openai-community/gpt2
#tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#model = GPT2LMHeadModel.from_pretrained('gpt2')

#https://huggingface.co/microsoft/phi-1_5

MODEL_NAME = "arnir0/Tiny-LLM"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto"    
)

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

    response_text = response[0][0]["generated_text"]
    return f"{response_text}"
