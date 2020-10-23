import os
import platform
from datetime import datetime


class PiCamera(object):

    def __init__(self, *args, **kwargs):
        print('WARNING: Mocked PiCamera on {}'.format(os.uname()))
        pass

    def start_preview(self, **options):
        self.resolution = None
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
