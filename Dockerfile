FROM balenalib/raspberry-pi-python:3.7

COPY . .

RUN PYTHONPATH=/usr/bin/python pip install -r requirements.txt

VOLUME /var/image/
ENTRYPOINT []
CMD ["python", "timelapse.py"]
