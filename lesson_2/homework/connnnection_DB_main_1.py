import psycopg2
import asyncio
import logging
import sys
from aiogram import Dispatcher, Bot, types, F
from aiogram.filters.command import CommandStart
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton,
                           InlineKeyboardMarkup)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

con = psycopg2.connect(
    dbname="postgres",
    user='postgres',
    password='1',
    host='localhost',
    port=5432
)

cur = con.cursor()

user_table = """
    create table users_write(
        id serial primary key , 
        name varchar (255) ,
        age integer ,
        phone_number varchar (13) check (phone_number ilike '+%') , 
        created_at timestamp default current_timestamp 
        )"""


# cur.execute(user_table)
# cur.commit()


def user_save(name, age, phone_number):
    insert_query = """insert into users(name ,age , phone_number)
                    values (%s , %s , %s)"""
    params = (name, age, phone_number)
    cur.execute(insert_query, params)
    con.commit()


BOT_TOKEN = "6327601579:AAFLGqXY3beXxerfQ9qIg-vjzibEjgIg_tw"
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    name = State()
    age = State()
    phone_number = State()
    request = State()


def phone_button():
    phone_g = KeyboardButton(text="Phone ☎️", request_contact=True)
    return ReplyKeyboardMarkup(keyboard=[[phone_g]], resize_keyboard=True)


def request_button():
    save = InlineKeyboardButton(text="SAVE 🟢", callback_data="save")
    edit = InlineKeyboardButton(text="EDIT 📝", callback_data="edit")
    design = [
        [save, edit]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


@dp.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer("Ismingizni kiriting : ")
    await state.set_state(UserState.name)


@dp.message(UserState.name)
async def name_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data.update({"name": message.text})
    await state.set_data(data)
    await message.answer("Yoshizni kiriting EXAMPLE (25-24-45) : ")
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def age_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data.update({"age": message.text})
    await state.set_data(data)
    await message.answer("Telefon raqamni yuborish uchun quydagi buttonni bosing :",
                         reply_markup=phone_button())
    await state.set_state(UserState.phone_number)


@dp.message(UserState.phone_number, F.contact)
async def phone_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()

    phone = message.contact.phone_number

    if not phone.startswith("+"):
        phone = "+" + phone

    data.update({"phone": phone})
    name = data.get("name")
    age = data.get("age")

    await state.set_data(data)

    text = f"name: {name}\nage: {age}\nphone ☎️: {phone}"
    await message.answer(text, reply_markup=request_button())
    await state.set_state(UserState.request)


@dp.message(UserState.request)
async def request_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    phone_number = data.get("phone_number")

    if call.data == "save":
        await call.message.answer("Muvaffaqiyatli saqlandi !")

    elif call.data == "edit":
        await call.message.answer("Ismizni kiriting : ")
        await state.set_state(UserState.name)


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
