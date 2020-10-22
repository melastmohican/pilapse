import os
import sys
from datetime import datetime
from time import sleep
from picamera import PiCamera

base_dir = os.path.join(
    sys.path[0],
    datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
camera = PiCamera()
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous(base_dir + 'img{counter:03d}.jpg'):
    print('Captured %s' % filename)
sleep(60)  # wait 1 minutes
