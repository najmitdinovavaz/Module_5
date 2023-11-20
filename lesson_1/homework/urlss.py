from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def number_button():
    n1 = KeyboardButton(text='🏢 О компании')
    n2 = KeyboardButton(text='📍 Филиалы')
    n3 = KeyboardButton(text='💼 Вакансии')
    n4 = KeyboardButton(text='📱 Меню')
    n5 = KeyboardButton(text='🗣 Новости')
    n6 = KeyboardButton(text='📞 Контакты/Адрес')
    n7 = KeyboardButton(text='🇺🇿/🇷🇺  Язык')

    design = [
        [n1, n2],
        [n3],
        [n4, n5],
        [n6, n7],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm


def region_button():
    k1 = KeyboardButton(text="Ташкент")
    k2 = KeyboardButton(text="Андижан")
    k3 = KeyboardButton(text="Коканд")
    k4 = KeyboardButton(text="Наманган")
    k5 = KeyboardButton(text="Ташкентская область")
    k6 = KeyboardButton(text="Самарканд")
    k7 = KeyboardButton(text="Хорезмская область")
    k8 = KeyboardButton(text="Наваи")
    k9 = KeyboardButton(text="❌  Отмена ❌")
    k10 = KeyboardButton(text="Назад ↩️")
    k11 = KeyboardButton(text="Фергана")

    figma = [
        [k1, k2],
        [k3, k4],
        [k5, k6],
        [k7, k11],
        [k8],
        [k9, k10],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=figma, resize_keyboard=True, one_time_keyboard=True)
    return rkm


def region_tashkent():
    k1 = KeyboardButton(text="Унниверсальный сотрудник")
    k2 = KeyboardButton(text="Оператор call-центра")
    k3 = KeyboardButton(text="Курьер")
    k4 = KeyboardButton(text="❌  Отмена ❌")
    k5 = KeyboardButton(text="Назад ↩️")

    tashkent = [
        [k1, k2],
        [k3],
        [k4, k5],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=tashkent, resize_keyboard=True, one_time_keyboard=True)
    return rkm


def region_andijan():
    k1 = KeyboardButton(text="Унниверсальный сотрудник")
    k2 = KeyboardButton(text="Курьер")
    k3 = KeyboardButton(text="❌  Отмена ❌")
    k4 = KeyboardButton(text="Назад ↩️")

    andijan = [
        [k1, k2],
        [k3, k4],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=andijan, resize_keyboard=True, one_time_keyboard=True)
    return rkm


def language_bot():
    k1 = KeyboardButton(text=" 🇷🇺 Русский")
    k2 = KeyboardButton(text="🇺🇿 O`zbekcha")
    k3 = KeyboardButton(text="🔙 Назад")

    language = [
        [k1, k2],
        [k3],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=language, resize_keyboard=True, one_time_keyboard=True)
    return rkm


def region_tashkent_filial():
    k1 = KeyboardButton(text="Юнусабадский р-н")
    k2 = KeyboardButton(text="Мирзо Улугбекский р-н")
    k3 = KeyboardButton(text="Яшнабадский р-н")
    k4 = KeyboardButton(text="Яккасарский р-н")
    k5 = KeyboardButton(text="Сергелинский р-н")
    k6 = KeyboardButton(text="Чиланзарский р-н")
    k7 = KeyboardButton(text="Мирабадский р-н")
    k8 = KeyboardButton(text="Шайхонтохурский р-н")
    k9 = KeyboardButton(text="Алмазарский р - н")
    k10 = KeyboardButton(text="Бектемирский р-н")
    k11 = KeyboardButton(text="❌  Отмена ❌")
    k12 = KeyboardButton(text="Назад ↩️")

    filial = [
        [k1, k2],
        [k3, k4],
        [k5, k6],
        [k7, k8],
        [k9, k10],
        [k11, k12],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=filial, resize_keyboard=True, one_time_keyboard=True)
    return rkm
