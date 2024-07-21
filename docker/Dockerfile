# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /chatbot

# Copy the requirements.txt file into the root
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app as well
COPY app.py .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run main.py when the container launches, as it is contained under the app folder, we define app.main
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
