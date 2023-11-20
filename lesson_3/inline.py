from aiogram.types import KeyboardButton , InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton


def inline_button1():
    btn1 = InlineKeyboardButton(text="Button 1" , callback_data='button 1')
    btn2 = InlineKeyboardButton(text="Button 2" , callback_data='button 2')
    btn3 = InlineKeyboardButton(text="BACK" , callback_data='back ')

    design = [
        [btn1 , btn2] ,
        [btn3]
    ]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    return ikm

