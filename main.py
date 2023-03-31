from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN_API

import string
import random

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/description - что умеешь?
/count - число собственных предыдущих вызовов
"""
clientBot = Bot(TOKEN_API)
dp = Dispatcher(clientBot)

@dp.message_handler(commands=['help'])
async  def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['start'])
async  def start_command(message: types.Message):
    await message.answer(text="Добро пожаловать в наш Телеграм Бот!")
    await message.delete()

@dp.message_handler(commands=['count'])
async  def check_command(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')
    count += 1

@dp.message_handler(commands=['description'])
async  def desc_command(message: types.Message):
    await message.answer('Данный бот умеет отправлять рандомные символы латинского алфавита')
    await message.delete()

@dp.message_handler()
async def send_random_letter(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))

if __name__ == '__main__':
    executor.start_polling(dp)
