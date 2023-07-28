# From specifies base image
FROM python:3.8

# Directory
WORKDIR /chatbot_project/chatbot_project

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copies directory into container
COPY . .

# The port the container should expose
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]