from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
from huggingface_hub import login

from docker.llms import get_model

token = Path('token').read_text().strip()
print("Hugginface token is:", token)
login(token=token)


# We define the app
app = FastAPI()

model = get_model("t5-tiny").load_model()

# We define that we expect our input to be a string
class RequestModel(BaseModel):
    input: str

# Now we define that we accept post requests
# ->  In APIs, requests are made to ask the API to perform a certain task — in this case to analyze a piece of text. 
@app.post("/sentiment")
def get_response(request: RequestModel):
    # We get the input prompt
    prompt = request.input
    
    return model.query_model(prompt)