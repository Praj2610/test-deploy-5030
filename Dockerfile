# Use an official Python runtime as a parent image
FROM python:3-alpine

# Update pip and install essential tools
RUN apk update && \
    apk add --no-cache \
    g++ \
    libressl-dev \
    musl-dev \
    cmake

# Upgrade pip and setuptools
RUN pip install --no-cache-dir --upgrade pip setuptools

# Create a virtual environment
RUN python -m venv /venv

# Activate the virtual environment
ENV PATH="/venv/bin:$PATH"

# Install your project's dependencies
COPY requirement.txt .
RUN pip install -r requirement.txt

# Copy your project files into the container
COPY . /app
WORKDIR /app
ENV PYTHONPATH=/app/

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
