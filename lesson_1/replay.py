from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def number_button():
    n1 = KeyboardButton(text='Buyurtmalar')
    n2 = KeyboardButton(text='Phone number', request_contact=True)
    n3 = KeyboardButton(text='Location', request_location=True)
    n4 = KeyboardButton(text='4')
    n5 = KeyboardButton(text='5')
    n6 = KeyboardButton(text='6')
    n7 = KeyboardButton(text='7')
    n8 = KeyboardButton(text='8')

    design = [
        [n1, n2, n3, n4],
        [n5, n6, n7, n8],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm
