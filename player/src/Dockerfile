# Install base Python image
FROM python:3.8-slim

# Copy files to the container
COPY . /src/

# Set working directory to previously added app directory
WORKDIR /src/

RUN apt-get update
RUN apt-get -y install \
	curl \
	git \
	nodejs \
	npm \
	openjdk-11-jre-headless

RUN apt update
RUN apt -y install build-essential libwrap0-dev libssl-dev libc-ares-dev uuid-dev xsltproc
RUN apt-get update -qq \
    && apt-get install --no-install-recommends --yes \
        build-essential \
        gcc \
        python3-dev \
        mosquitto \
        mosquitto-clients


RUN pip3 install --upgrade pip setuptools wheel

RUN python3 -m pip install --no-cache-dir \
      numpy scipy matplotlib scikit-build opencv-contrib-python-headless \
      influxdb paho-mqtt configparser Pillow \
      qrcode

RUN pip install -r requirements.txt

CMD ["python3", "static/shaka-player/build/all.py"] 

# Expose the port uvicorn is running on
EXPOSE 80

# Run uvicorn server
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
