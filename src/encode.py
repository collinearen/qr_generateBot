import time
import uuid

import qrcode

import settings


class EncodeImage(object):
    def __init__(self, message):
        self.message = message

    def encode(self):
        data = self.message
        path_to_file = f"{settings.PATH_ENCODE_PHOTO}/{uuid.uuid4()}.jpg"
        img = qrcode.make(data)
        img.save(path_to_file)
        return path_to_file
