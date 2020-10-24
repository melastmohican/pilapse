FROM balenalib/raspberry-pi-python:3.7

COPY . .
RUN pip install -r requirements.txt

VOLUME /var/image/
ENTRYPOINT []
CMD ["python", "timelapse.py"]
