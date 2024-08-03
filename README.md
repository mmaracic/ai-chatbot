# Sources
 Original sources:  
 https://www.kdnuggets.com/a-simple-to-implement-end-to-end-project-with-huggingface
 https://github.com/rfeers/data-science-portfolio/tree/main/end-to-end-projects/simple-docker-hf-model

# Python 3 requirements
* Install Python3
* If python3 is not recognised as python command
```
sudo apt install python-is-python3
```
* Install pip
```
sudo apt install python3-pip
```
* Install hugginface cli
```
pip install -U "huggingface_hub[cli]"
```
* Add install folder to ~/.profile

For Windows
* Install Python 3
* Install pip:
```
python -m ensurepip --upgrade
```
```
python -m pip install --upgrade pip
```
* Add python and pip path <python_folder>\Scripts (e.g. C:\Python38\Scripts) to Windows path 
# Hugging face
Logging in:  
```
huggingface-cli login
```
Token will be saved to /home/<user>/.cache/huggingface/token  
Copy token file to docker subfolder and it will be used in docker image.
# Start app
Run the docker-compose file

## Errors
If the image doesnt start force full rebuild with upgraded requirements:
```
docker-compose build --no-cache
```

# App access
Access:  
http://localhost:8000/docs  
To see FastAPI swagger page with information

Available POST API is on:  
http://localhost:8000/sentiment   
Sample request:  
```
{
  "input":"I am happy"
}
```
Full sample is in thunder-collection file included in the project