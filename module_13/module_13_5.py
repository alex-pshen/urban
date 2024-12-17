import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.row(KeyboardButton("Рассчитать"), KeyboardButton("Информация"))


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    try:
        await state.update_data(age=int(message.text))
        await message.answer("Введите свой рост:")
        await UserState.growth.set()
    except ValueError:
        await message.answer("Введите корректный возраст (целое число).")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        await state.update_data(growth=int(message.text))
        await message.answer("Введите свой вес:")
        await UserState.weight.set()
    except ValueError:
        await message.answer("Введите корректный рост (целое число).")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    try:
        weight = float(message.text)
        await state.update_data(weight=weight)
        data = await state.get_data()
        cal = 10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"] + 5
        await message.answer(f"Ваша норма калорий: {cal}")
        await state.finish()
    except ValueError:
        await message.answer("Введите корректный вес (число с плавающей точкой).")


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer(
        "Введите команду /start, чтобы начать общение.", reply_markup=kb
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
