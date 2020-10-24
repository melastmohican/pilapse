FROM balenalib/raspberry-pi-python:3.7

# pip install python deps from requirements.txt
# For caching until requirements.txt changes
ENV READTHEDOCS True
COPY ./requirements.txt /requirements.txt
RUN pip install -v -r /requirements.txt

VOLUME /var/image/
COPY . .
#ENTRYPOINT []
CMD ["python", "timelapse.py"]
