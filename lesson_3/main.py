import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from lesson_3.button import start_button, start_button2
from lesson_3.inline import inline_button1
from aiogram.fsm.state import StatesGroup, State


class StepState(StatesGroup):
    state1 = State()
    state2 = State()
    state3 = State()
    state4 = State()


Token = "6327601579:AAFLGqXY3beXxerfQ9qIg-vjzibEjgIg_tw"
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await message.answer("Welcome to you BOT !!!", reply_markup=start_button())
    await state.set_state(StepState.state1)


@dp.message(lambda message: message.text == 'btn1', StepState.state1)
async def inline_button_handler(message: Message, state: FSMContext):
    await message.answer('Button 1 boslidi', reply_markup=inline_button1())
    await state.set_state(StepState.state2)


@dp.message(lambda message: message.text == 'btn2', StepState.state1)
async def inline_button2_handler(message: Message, state: FSMContext):
    await message.answer('Button 2 boslidi', reply_markup=start_button2())
    await state.set_state(StepState.state3)


@dp.message(StepState.state3)
async def back_handler(message: Message, state: FSMContext):
    if message.text == 'back':
        await state.set_state(StepState.state1)
        await message.answer("Back", reply_markup=start_button())


async def main():
    bot = Bot(token=Token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
