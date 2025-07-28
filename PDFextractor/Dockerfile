# Specify the platform for compatibility with the evaluation environment [cite: 56, 57]
FROM --platform=linux/amd64 python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Create directories for input and output data as per the run command [cite: 69]
RUN mkdir -p /app/input /app/output

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies listed in requirements.txt
# --no-cache-dir helps in keeping the image size smaller
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main application script into the container's working directory
COPY main.py .

# Set the default command to execute when the container starts
CMD ["python", "main.py"]