import asyncio
import logging
import os
from contextlib import contextmanager

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

import settings
from encode import EncodeImage

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.KEY)

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    '''
    :param message: передаем наше дефолтное фото приветствия, с описанием реализации бота
    :return:
    '''
    photo = FSInputFile(fr"{settings.PATH_DEFAULT_PHOTO}")
    await bot.send_photo(message.chat.id, photo,
                         caption=f"Привет, это бот по генерации QR-кодов, "
                                 "напиши мне что-либо, а я сгенерирую на твое сообщение QR.\n"
                                 "Поехали!")


@contextmanager
def take_photo(photo):
    '''
    Так как не нужно в дальнейшем хранить QR-коды,
    можно создать контекст менеджер, и при закрытии его через блок finally всегда удалять фотографию по пути photo.path
    '''
    try:
        yield photo
    finally:
        os.remove(photo.path)


@dp.message()
async def send_welcome(message):
    try:
        qr = EncodeImage(message=message.text)
        photo = FSInputFile(fr"{qr.encode()}")
        with take_photo(photo) as ph:
            await bot.send_photo(message.chat.id, ph, caption=f"Лови свой QR")

    except ConnectionError:
        await message.answer(f'Друг, попробуй позже, сервер слишком загружен')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
