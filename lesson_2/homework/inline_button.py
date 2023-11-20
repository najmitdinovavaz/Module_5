from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_button():
    s1 = KeyboardButton(text="Books 📚")
    s2 = KeyboardButton(text="IELTS 🎓")
    s3 = KeyboardButton(text="Test 🔤")
    s4 = KeyboardButton(text="Admin 👨🏻‍💻")

    design = [
        [s1, s2],
        [s3, s4],
    ]

    agg = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return agg


def section_books():
    s1 = KeyboardButton(text="Vocabulary 🧾 ")
    s2 = KeyboardButton(text="Book 2 ")
    s3 = KeyboardButton(text="Book 3 ")
    s4 = KeyboardButton(text="🔙 Back")

    buttons = [
        [s1, s2],
        [s3, s4],
    ]

    var = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True)
    return var


def inline_number():
    btn1 = InlineKeyboardButton(text='Admin', url='https://t.me/avazvf')

    design = [
        [btn1],
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm
