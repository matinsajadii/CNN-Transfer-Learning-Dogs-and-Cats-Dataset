# Use the official TensorFlow Docker image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files
COPY web_app /app
COPY requirements.txt /app

# Install necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run your Streamlit app
CMD ["streamlit", "run", "web_app.py"]
