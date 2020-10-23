import os
from datetime import datetime
from time import sleep

if os.uname()[1] == 'raspberrypi':
    from picamera import PiCamera
else:
    from mock_picamera.camera import PiCamera


def get_path(base_dir):
    full_path = base_dir + '/' + datetime.now().strftime('%Y/%m/%d/%H')
    os.makedirs(full_path, exist_ok=True)
    return full_path


base_dir = '/var/image'

path = get_path(base_dir)
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous(path + '/img{counter:05d}.jpg'):
    print('Captured %s' % filename)
    sleep(60)  # wait 1 minutes
