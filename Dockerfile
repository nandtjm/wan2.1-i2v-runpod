FROM runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg libgl1 libglib2.0-0

# Copy code
COPY app/ /app/

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Entry point for RunPod Serverless
CMD ["python", "handler.py"]
