import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup

BOT_TOKEN = "6327601579:AAFLGqXY3beXxerfQ9qIg-vjzibEjgIg_tw"
dp = Dispatcher(storage=MemoryStorage())


class StepState(StatesGroup):
    step1 = State()
    step2 = State()


def buttons():
    btn1 = KeyboardButton(text="🏢 О компании")
    btn2 = KeyboardButton(text="📍 Филиалы")
    btn3 = KeyboardButton(text="💼 Вакансии")

    design = [
        [btn1, btn2, btn3]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


@dp.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext):
    await state.set_state(StepState.step1)
    await message.answer("Salam alekum", reply_markup=buttons())


@dp.message(StepState.step1)
async def step1_handler(message: types.Message, state: FSMContext):
    await state.set_state(StepState.step2)
    data = await state.get_data()
    data.update({"button": message.text})
    await state.set_data(data)


@dp.message(StepState.step2)
async def step2_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"Sava the document : : {data.get('button')}")


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
