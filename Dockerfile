FROM balenalib/raspberry-pi-python:3.7

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . .
VOLUME /var/image/
ENTRYPOINT []
CMD ["python", "timelapse.py"]
