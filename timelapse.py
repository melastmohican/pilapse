import os
from datetime import datetime
from time import sleep

#if os.uname()[1] == 'raspberrypi':
from picamera import PiCamera
#else:
#    from mock_picamera.camera import PiCamera


def get_path(base_dir):
    full_path = base_dir + '/' + datetime.now().strftime('%Y/%m/%d/%H')
    os.makedirs(full_path, exist_ok=True)
    return full_path

# print(os.uname()[1])
base_dir = '/var/image'
camera = PiCamera(resolution=(1920, 1080))
# Set ISO to the desired value
camera.iso = 100
# Wait for the automatic gain control to settle
sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous(get_path(base_dir) + '/img{counter:05d}.jpg'):
    print('Captured %s' % filename)
    sleep(60)  # wait 1 minutes
