import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart
from aiogram.enums import ParseMode

from lesson_2.homework.inline_button import start_button, section_books, inline_number

BOT_TOKEN = "6327601579:AAFLGqXY3beXxerfQ9qIg-vjzibEjgIg_tw"

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    url = "AgACAgQAAxkBAAIBnmVUswk-e4vIJgTPAAGgbnVJZHqdBAACwrExG8vKbVHYFu-_poQOIQEAAwIAA3MAAzME"
    caption = f"Hello {message.from_user.full_name}! E-english bot you now have the English opportunity " \
              f"to strengthen your language 😊 "
    await message.answer_photo(photo=url, caption=caption, reply_markup=start_button())


@dp.message(lambda message: message.text == "Books 📚")
async def books_handler(message: types.Message):
    url = "AgACAgQAAxkBAAN5ZVT8lXsMoPNe016WybC29rCDS4EAAmCxMRv3bpRRKW0X4HN-omwBAAMCAANzAAMzBA"
    await message.answer_photo(photo=url, reply_markup=section_books())
    await message.answer("Section of Book !")


@dp.message(lambda message: message.text == "IELTS 🎓")
async def ielts_handler(message: types.Message):
    await message.answer(
        "Congratulations on this achievements we wish you good luck and "
        "good health you are the best of the best 🥳🥳🥳🥳🥳🥳")


@dp.message(lambda message: message.text == "Test 🔤")
async def test_handler(message: types.Message):
    url = "AgACAgQAAxkBAAOvZVUF70AfBv8OTnGM-ZPFpGMN118AAnuxMRsB_KxRXVulJ4-uN4MBAAMCAANzAAMzBA"
    await message.answer_photo(photo=url)
    await message.answer("Test section !")


@dp.message(lambda message: message.text == "Admin 👨🏻‍💻")
async def admin_handler(message: types.Message):
    url = "AgACAgQAAxkBAAPBZVUG_it1-W8TFshJEwddIZ_qrP0AAkeyMRuSyLRRtLS-NaIuht8BAAMCAANzAAMzBA"
    await message.answer_photo(photo=url, reply_markup=inline_number())


# @dp.message(F.photo)
# async def photo(message: types.Message, state: FSMContext):
#     await message.answer(message.photo[0].file_id)


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
