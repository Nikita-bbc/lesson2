from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
bt_1 = types.KeyboardButton(text='Рассчитать калории')
bt_2 = types.KeyboardButton(text='Информация')
kb_reply.row(bt_1, bt_2)

kb_inline = types.InlineKeyboardMarkup()
bt_1_inline = types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
bt_2_inline = types.InlineKeyboardButton(text='Формулы для расчёта', callback_data='formulas')
kb_inline.row(bt_1_inline, bt_2_inline)


class UserState(StatesGroup):
    age = State()
    weight = State()
    growth = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await asyncio.sleep(1)
    await message.answer("Привет! Я бот, помогающий вашему здоровью!", reply_markup=kb_reply)


@dp.message_handler(text='Рассчитать калории')
async def main_menu(message):
    await message.answer('Выберете опцию', reply_markup=kb_inline)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await asyncio.sleep(1)
    await call.message.answer('Формула для расчёта калорий: '
                              '10 x вес(кг) + 6,25 х рост(см) - 5 х возраст(лет) - 161')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await asyncio.sleep(1)
    await call.message.answer('Введите ваш возраст')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await asyncio.sleep(1)
    await message.answer('Введите ваш рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await asyncio.sleep(1)
    await message.answer('Введите ваш вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    user_calories = await state.get_data()
    age = user_calories.get("age")
    growth = user_calories.get("growth")
    weight = user_calories.get("weight")
    calories = 10 * weight + 6 * growth - 5 * age + 5
    await asyncio.sleep(1)
    await message.answer(f'Ваша дневная норма калорий: {calories}')
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    await asyncio.sleep(1)
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
