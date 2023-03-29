# Install base Python image
FROM python:3.8-slim-buster

# Copy files to the container
COPY *.py /ml_service/
COPY requirements.txt /ml_service/

# Set working directory to previously added app directory
WORKDIR /ml_service/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port uvicorn is running on
EXPOSE 81

# Run uvicorn server
CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "81"]
