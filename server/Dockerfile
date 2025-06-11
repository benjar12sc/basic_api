# Use official Python 3.12 image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the server code
COPY src/ ./src/
COPY ../data/ ./data/

# Run the database population script
RUN python src/populate_database.py

# Expose the port
EXPOSE 8000

# Start the FastAPI app
CMD ["python", "src/main.py"]
