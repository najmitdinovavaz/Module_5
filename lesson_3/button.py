from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def start_button():
    btn1 = KeyboardButton(text="btn1")
    btn2 = KeyboardButton(text="btn2")
    design = [[btn1 , btn2]]
    rkm =  ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True , one_time_keyboard=True)
    return rkm


def start_button2():
    btn1 = KeyboardButton(text="btn1")
    btn2 = KeyboardButton(text="btn2")
    btn3 = KeyboardButton(text="back")
    design = [
        [btn1 , btn2] ,
        [btn3]
    ]
    rkm =  ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True , one_time_keyboard=True)
    return rkm

