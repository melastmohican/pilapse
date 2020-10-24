FROM balenalib/raspberry-pi-python:3.7

COPY ./requirements.txt /requirements.txt
ENV READTHEDOCS=True
#RUN pip install -r /requirements.txt

VOLUME /var/image/
COPY . .
ENTRYPOINT []
CMD ["python", "timelapse.py"]
