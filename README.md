# Sources
 Original sources:  
 https://www.kdnuggets.com/a-simple-to-implement-end-to-end-project-with-huggingface
 https://github.com/rfeers/data-science-portfolio/tree/main/end-to-end-projects/simple-docker-hf-model

# Start app
Run the docker-compose file

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