# From specifies base image
FROM python:3.8

# Directory
WORKDIR /chatbot_project/chatbot_project

# Copies directory into container
COPY . .

# Install dependencies
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# The port the container should expose
# EXPOSE 5000

# Run the application
CMD ["python", "app.py"]