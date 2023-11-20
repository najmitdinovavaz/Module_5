from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def inline_number():
    btn1 = InlineKeyboardButton(text='1', callback_data='1')
    btn2 = InlineKeyboardButton(text='tavarlar', callback_data='tavar')
    btn3 = InlineKeyboardButton(text='Kun uz', url='https://kun.uz')
    btn4 = InlineKeyboardButton(text='Admin', url='https://t.me/avazvf')

    design = [
        [btn1, btn2],
        [btn3, btn4],
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm
