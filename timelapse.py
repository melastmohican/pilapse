import os
from datetime import datetime
from omegaconf import OmegaConf
from time import sleep

from picamera import PiCamera
# if os.uname()[1] == 'raspberrypi':
#     from picamera import PiCamera
# else:
#     from mock_picamera.camera import PiCamera


def get_path(base_dir):
    full_path = base_dir + '/' + datetime.now().strftime('%Y/%m/%d/%H')
    os.makedirs(full_path, exist_ok=True)
    return full_path


# print(os.uname()[1])
conf = OmegaConf.load('./config.yaml')
base_dir = '/var/image'
camera = PiCamera(resolution=(conf.resolution.width, conf.resolution.height))
# Set ISO to the desired value
camera.iso = conf.iso
# Rotate the images taken by the camera. Possible value are 0, 90, 180 or 270
camera.rotation = conf.rotation
# Wait for the automatic gain control to settle
sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
camera.start_preview()
try:
    for filename in camera.capture_continuous(get_path(base_dir) + '/img{counter:05d}.jpg'):
        print('Captured %s' % filename)
        sleep(conf.wait)  # wait 30 seconds
finally:
    camera.stop_preview()
