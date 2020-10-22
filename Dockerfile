FROM balenalib/raspberry-pi-python:3.7
COPY . .
VOLUME /var/image/`
ENTRYPOINT []
CMD ["python", "timelapse.py"]
