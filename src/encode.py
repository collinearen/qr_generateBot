import time
import uuid

import qrcode

import settings


class EncodeImage(object):
    def __init__(self, message):
        '''
        :param message: сообщение пользователя, которое он хочет закодировать
        '''
        self.message = message

    def encode(self):
        '''
        Здесь происходит кодировка нашего QR,
        сохранение его по определенному адресу и передача пути к этому файлу
        '''
        data = self.message
        path_to_file = f"{settings.PATH_ENCODE_PHOTO}/{uuid.uuid4()}.jpg"
        img = qrcode.make(data)
        img.save(path_to_file)
        return path_to_file
