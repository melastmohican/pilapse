FROM balenalib/raspberry-pi-python:3.7

RUN apt-get update -qy && apt-get install -qy python
COPY . .

VOLUME /var/image/

ENTRYPOINT []
CMD ["python", "take.py", "60"]
