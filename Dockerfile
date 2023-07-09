# Use the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application code to the working directory
COPY . .


# Expose the port on which your Flask application will run
EXPOSE 5000

# Run the Flask application
CMD ["python", "main.py"]
