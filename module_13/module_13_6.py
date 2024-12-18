import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


rkb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[[KeyboardButton("Рассчитать"), KeyboardButton("Информация")]],
)
ikb = InlineKeyboardMarkup(row_width=2)
ikb.add(InlineKeyboardButton("Рассчитать норму калорий", callback_data="calories"))
ikb.add(InlineKeyboardButton("Формулы расчёта", callback_data="formulas"))


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=rkb)


@dp.message_handler(text="Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=ikb)


@dp.callback_query_handler(lambda c: c.data == "calories")
async def set_age(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await call.message.answer(
        "Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove()
    )
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        await state.update_data(age=age)
        await message.answer("Введите свой рост (в см):")
        await UserState.growth.set()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный возраст (целое число).")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        growth = int(message.text)
        await state.update_data(growth=growth)
        await message.answer("Введите свой вес (в кг):")
        await UserState.weight.set()
    except ValueError:
        await message.answer("Пожалуйста, введите корректный рост (целое число).")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    try:
        weight = float(message.text)
        await state.update_data(weight=weight)
        data = await state.get_data()
        cal = 10 * data["weight"] + 6.25 * data["growth"] - 5 * data["age"] + 5
        await message.answer(f"Ваша норма калорий: {cal}", reply_markup=ikb)
        await state.finish()
    except ValueError:
        await message.answer(
            "Пожалуйста, введите корректный вес (число с плавающей точкой)."
        )


@dp.callback_query_handler(lambda c: c.data == "formulas")
async def get_formulas(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await call.message.answer(
        "Формула расчёта нормы калорий:\n10 * вес + 6.25 * рост - 5 * возраст + 5",
        reply_markup=ikb,
    )


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
