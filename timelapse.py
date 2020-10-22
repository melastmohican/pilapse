import os
import sys
import time
from datetime import datetime
from time import sleep
from picamera import PiCamera

def try_to_mkdir(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

def prepare_dir(base, now):
    path = str(now.year)
    try_to_mkdir(base + "/" +path)

    path = str(now.year)  + "/"  + str(now.month)
    try_to_mkdir(base + "/" +path)

    path = str( datetime.now().year)  + "/"  + str( datetime.now().month)+"/"+ str( datetime.now().day)
    try_to_mkdir(base + "/" +path)

    path =  str( datetime.now().year)  + "/"  + str( datetime.now().month)+"/"+ str( datetime.now().day)+"/"+ str( datetime.now().hour)
    try_to_mkdir(base + "/" +path)
    return path

def get_path(base_dir):
    now = datetime.now()
    path = prepare_dir(base_dir, now)
    full_path = base_dir + "/" + path + "/"
    print(full_path)
    return full_path
    
    

base_dir = '/var/image'
    
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous(get_path(base_dir) + 'img{counter:05d}.jpg'):
    print('Captured %s' % filename)
    sleep(60)  # wait 1 minutes
