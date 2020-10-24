FROM balenalib/raspberry-pi-python:3.7
COPY . .
ENTRYPOINT ["entrypoint.sh"]
# pip install python deps from requirements.txt
# For caching until requirements.txt changes
ENV READTHEDOCS True
COPY ./requirements.txt /requirements.txt
RUN pip install -v -r /requirements.txt

VOLUME /var/image/

CMD ["python", "timelapse.py"]
