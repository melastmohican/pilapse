FROM balenalib/raspberry-pi-python:3.7

#switch on systemd init system in container
ENV INITSYSTEM off

RUN apt-get update && apt-get install -y \
        python3-wheel \
	&& rm -rf /var/lib/apt/lists/*

# pip install python deps from requirements.txt
# For caching until requirements.txt changes
ENV READTHEDOCS True
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

VOLUME /var/image/
COPY . .
ENTRYPOINT []
CMD ["python", "timelapse.py"]
