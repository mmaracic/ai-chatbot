from pydantic import BaseModel

# We define that we expect our input to be a string
class RequestModel(BaseModel):
    input: str
