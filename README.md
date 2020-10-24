# pilapse
Timelapse on Raspberry PI Zero with PiCamera

mkdir -p /var/image/
docker build -t melastmohican/pilapse:0.1 .

docker run --name timelapse -v /var/image:/var/image --privileged --restart=always -e TZ="US/Pacific" -d melastmohican/pilapse:0.1

docker rm -f capture
