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
* Install pip (will not work if pip was installed using apt-get):
```
sudo apt install python3-pip
```
* Install possibility to create virtual environments
```
sudo apt install python3-venv
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

## PIP
The custom pip libraries need to be installed in virtual environment (otherwise for environment maintained for apt-get we will get - error: externally-managed-environment)

Check if virtual environment is active (if its not active it will write /usr/bin/python, if it is cmd will be prefixed by name of virtual env and this will print env path)
```
which python (Linux)
```
```
where python (Windows)
```
Create virtual environment in.venv subfolder
```
python3 -m venv .venv
```
Activate environment in .venv subfolder:
```
source .venv/bin/activate (Linux)
```
```
.\.venv\bin\activate (Windows)
```
In the virtual environment it will now be possible to install any needed libraries using:
```
python3 -m pip install requests
```
```
python3 -m pip install -r requirements.txt
```

To deactivate the current virtual environment use:
```  
deactivate
```

# Hugging face
Logging in:  
```
huggingface-cli login
```
Token will be saved to /home/<user>/.cache/huggingface/token  
Copy token file to docker subfolder and it will be used in docker image.
# Start app
Run the docker-compose file

## On machine
* Activate the local python environment .venv
* In the folder where application is, run:
```
uvicorn docker.app:app --app-dir .. --host 127.0.0.1 --port 8000
```
App-dir option sets the runtime folder of the app to root project folder which results in package names as expected by .py files. In this case the app needs to be specified as a submodule of docker module (folder).  
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
