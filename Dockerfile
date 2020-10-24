FROM balenalib/raspberry-pi-python:3.7
COPY . .
# pip install python deps from requirements.txt
# For caching until requirements.txt changes
ENV READTHEDOCS True
COPY ./requirements.txt /requirements.txt
RUN pip install -v -r /requirements.txt

VOLUME /var/image/

ENTRYPOINT ["entrypoint.sh"]
CMD ["python", "timelapse.py"]
