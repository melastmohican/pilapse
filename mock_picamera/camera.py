import os
import platform
from datetime import datetime


class PiCamera(object):

    def __init__(self, *args, **kwargs):
        print('WARNING: Mocked PiCamera on {}'.format(os.uname()))
        self.resolution = kwargs.pop('resolution', None)
        self.shutter_speed = None
        self.exposure_speed = None
        self.awb_gains = None
        self.rotation = None
        pass

    def start_preview(self, **options):
        pass

    def stop_preview(self):
        pass


    def capture_continuous(self, output, format=None, use_video_port=False, resize=None,
                           splitter_port=0, burst=False, bayer=False, **options):
        print(output)
        counter = 1
        while True:
            filename = output.format(
                counter=counter,
                timestamp=datetime.now(),
            )
            yield filename
            counter += 1
