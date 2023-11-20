import asyncio
import logging
import sys
from subprocess import call

import emoji
import types

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import F
from aiogram.filters.command import Command
from aiogram import types

from lesson_1.replay import number_button
from lesson_1.magic import inline_number

TOKEN = "6092731491:AAG4CPPDDYnP014wDoCBilh6Xr1zsfz2j9c"

dp = Dispatcher()


@dp.message(Command("start"))
# @dp.message(Command("panel"))
async def digit_handler(message: Message):
    await message.answer("Hello world", reply_markup=inline_number())


@dp.callback_query(lambda call: call.data == '1')
@dp.callback_query(lambda call: call.data == 'Tavar')
@dp.callback_query(lambda call: call.data == 'Kun uz')
@dp.callback_query(lambda call: call.data == 'Admin')
async def one_keyboard_button(call: types.CallbackQuery):
    await call.message.answer(f"{call.data} - bosildi")


@dp.message(lambda message: message.text == 'Buyurtmalar')
async def digit_handler(message: Message):
    await message.answer("Bir raqami bosildi")


@dp.message(lambda message: message == 'Phone number')
async def contact_handler(message: Message):
    await message.answer('Phone number')


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello , Avaz {hbold(message.from_user.full_name)}!")


@dp.message(lambda message: message.text.isdigit() and 1 <= int(message.text) <= 100)
@dp.message(F.text.isdigit())
async def digit_handler(message: Message):
    await message.answer(message.text)


@dp.message(F.photo)
async def photo_handler(message: Message):
    await message.answer("photo handler successful ")
    await message.answer(f"{message.photo[0].file_id}")


@dp.message(F.document)
async def photo_handler(message: Message):
    await message.answer(f"Document handler successful \n{message.document.file_id}")


@dp.message(F.video)
async def photo_handler(message: Message):
    await message.answer("Video handler successful")
    await message.answer(f"{message.video.file_id}")


@dp.message(F.audio)
async def photo_handler(message: Message):
    await message.answer("Audio handler successful")
    await message.answer(f"{message.audio.file_id}")


@dp.message(F.sticker)
async def photo_handler(message: Message):
    await message.answer("Sticker handler successful")
    await message.answer(f"{message.sticker.file_id}")


@dp.message(F.voice)
async def photo_handler(message: Message):
    await message.answer("Voice handler successful")
    await message.answer(f"{message.voice.file_id}")


@dp.message(lambda message: emoji.emoji_count(message.text) > 0)
async def photo_handler(message: Message):
    await message.answer("Emoji handler successful")
    await message.answer(f"{message.emoji.file_id}")


@dp.message(F.GIF)
async def photo_handler(message: Message):
    await message.answer("GIF handler successful")
    await message.answer(f"{message.GIF.file_id}")


@dp.message()
async def echo_function_message(message: Message):
    for i in range(15):
        await message.copy_to(message.from_user.id)


# await message.answer("Salam alekum .")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
