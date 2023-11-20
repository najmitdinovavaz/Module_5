import asyncio
import sys
import logging
import emoji
import types
from subprocess import call
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import F
from aiogram.filters.command import Command
from aiogram import types
from geopy import Nominatim

from lesson_1.homework.urlss import region_button, region_tashkent, region_andijan, language_bot, region_tashkent_filial
from urlss import number_button

Token = "6636969963:AAGS5VXOwntbVSurq3dW-EJw7jtFCg20OmA"

dp = Dispatcher()


@dp.message(F.photo)
async def start_handler(message: Message):
    # await message.answer_photo("AgACAgQAAxkBAAMHZVB5VGeEpVhh_R6FQ-udw1uSyikAAlusMRtQnIRTEdxt422z7KEBAAMCAANzAAMzBA",
    #                            reply_markup=number_button())
    print(message.photo[0].file_id)


# @dp.message(F.photo)
# async def start_handler(message: Message):
#     # await message.answer_photo("AgACAgQAAxkBAAMHZVB5VGeEpVhh_R6FQ-udw1uSyikAAlusMRtQnIRTEdxt422z7KEBAAMCAANzAAMzBA",
#     #                            reply_markup=number_button())
#     print(message.photo[0].file_id)


# @dp.message(F.document)
# async def photo_handler(message: Message):
#     await message.answer("GIF handler successful")
#     await message.answer(f"{message.document.file_id}")
#
#
# @dp.message(lambda message: message.text == '🏢 О компании')
# async def digit_handler(message: Message):
#     await message.answer(f"{photo_handler}", """Информация о компании
# Сеть ресторанов быстрого обслуживания EVOS® не стоит
# на месте, а постоянно растет и развивается вместе с
# вами и для вас! Мы расширяем свою географию и открываем
# новые филиалы практически каждый месяц.
# Сейчас в нашей сети насчитывается более 50 филиалов по
# всему Узбекистану. Поэтому мы всегда в поиске динамичных
# и активных людей, которые хотят стать частью нашей команды
# и готовы строить свою карьеру в EVOS®.
# EVOS® – это надежный бренд, которому доверяют. Работа в
# EVOS® – гарантия стабильного заработка
# и перспективы карьерного роста.
# Начни свою карьеру в EVOS® уже сейчас!""")
#
#
# @dp.message(Command("📍 Филиалы"))
# async def start_handler(message: Message):
#     await message.answer_photo("AgACAgQAAxkBAANsZVDMQGFEkTUHlbwKgSHyQb6cp8MAApOsMRvcRIVR9fvkxg1NRUoBAAMCAANzAAMzBA")
#
#
# # print(message.photo[0].file_id)
#
#
# @dp.message(lambda message: message.text == '📍 Филиалы')
# async def digit_handler(message: Message):
#     await message.answer_photo("AgACAgQAAxkBAANsZVDMQGFEkTUHlbwKgSHyQb6cp8MAApOsMRvcRIVR9fvkxg1NRUoBAAMCAANzAAMzBA",
#                                """EVOS - крупнейшая фастфуд-компания в
#                                 Узбекистане.На данный момент открыто
#                                  49 торговых точек и современное
#                                   многопрофильное производство.
#
#                            Сотрудники компании это большая семья,
#                             которая развивается вместе и растет изо
#                              дня в день.Компания EVOS расширяется
#                               каждый день, сегодня нас более полутора
#                                тысяч.Стань частью нашей команды,
#                                 добро пожаловать в семью EVOS!""")
#
#
# @dp.message(lambda message: message.text == '💼 Вакансии')
# async def digit_handler(message: Message):
#     await message.answer("Присоединяйтесь в команду EVOS!", "📍 Выберите регион:", reply_markup=region_button())
#
#
# @dp.message(lambda message: message.text == 'Ташкент')
# async def digit_handler(message: Message):
#     await message.answer(f"💼 Выберите интересующую Вас вакансию", reply_markup=region_tashkent())
#     await message.answer("AgACAgQAAxkBAAMHZVJLP_vf_t_IKtrMUrkOzB2yVr0AAnisMRvyZjVR5bu3TvnmuvUBAAMCAANzAAMzBA",
#                          """📌Возраст от 18 до 35
#
#                             🇷🇺/🇺🇿 Владение русским и узбекским языком
#
#                             🕑 Свободный график(желательно)
#
#                             ✔️Опрятный внешний вид
#
#                             💰 Зарплата от 13 500( с учетом вычета НДФЛ) тысяч сум за 1 час""")
#     await message.answer("Выберите район где данный момент открыты вакансии.", reply_markup=region_tashkent_filial())
#
#
# @dp.message(lambda message: message.text == 'Андижан', "Коканд", "Наманган", "Ташкентская область", "Самарканд",
#             "Хорезмская область", "НаваиФергана")
# async def digit_handler(message: Message):
#     await message.answer(f"💼 Выберите интересующую Вас вакансию", reply_markup=region_andijan())
#
#
# @dp.message(lambda message: message.text == '📱 Меню')
# async def digit_handler(message: Message):
#     await message.answer("AgACAgQAAxkBAAMDZVI9Kc9CD_UlzSbZ_isvxE92Rn0AArusMRsa1ERTLnDmdDpgaagBAAMCAANzAAMzBA",
#                          "https://evos.uz/")
#     await message.answer("https://instagram.com/evosuzbekistan?igshid=NWtya2c0eW95Ymlh" " | ",
#                          "https://www.instagram.com/evosuzbekistan/"), ("https://www.facebook.com/evosuzbekistan/")
#
#
# @dp.message(lambda message: message.text == '🗣 Новости')
# async def digit_handler(message: Message):
#     await message.answer("""Kompaniya yangiliklari
#                             Aksiya
#                             Yangi filiallar
#                             Yangi tortlar va hk.""")
#
#
# @dp.message(lambda message: message.text == '📞 Контакты/Адрес')
# async def digit_handler(message: Message):
#     await message.answer("AgACAgQAAxkBAAMGZVJCy7QHqZ-H1Dj3D80E0zXAVe4AAq-xMRuFbp1S_0L3P94_7YYBAAMCAANzAAMzBA",
#                          """📍Адрес:  ул. Фурката 175, 1 подъезд, 2 этаж.
#                             📌Ориентир: MAKRO THE TOWER
#
#                             📲 Контакты: +998 71 203 12 12""")
#     await message.answer_location(longitude="85.137566", latitude="25.594095")
#
#
# @dp.message(lambda message: message.text == '🇺🇿/🇷🇺  Язык')
# async def digit_handler(message: Message):
#     await message.answer("Смена языка", reply_markup=language_bot())


async def main() -> None:
    bot = Bot(Token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
