# Base image to use for building the Docker image
FROM python:3.10-slim  
# Disable writing bytecode files (.pyc)
ENV PYTHONDONTWRITEBYTECODE 1  
# Disable buffering Python standard output and error streams
ENV PYTHONUNBUFFERED 1  
# Create a directory called /code in the container
RUN mkdir /code  
# Set /code as the working directory
WORKDIR /code  
# Copy the requirements.txt file from the host machine to /code in the container
COPY requirements.txt /code/  
# Install the Python dependencies specified in requirements.txt
RUN pip install -r requirements.txt  
# Copy the entire current directory (including the Dockerfile) to /code in the container
COPY . /code/  