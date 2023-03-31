from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN_API

HELP_COMMAND = """
/help - список команд
/start - начать работу с ботом
/count - число собственных предыдущих вызовов
"""
clientBot = Bot(TOKEN_API)
dp = Dispatcher(clientBot)

@dp.message_handler(commands=['help'])
async  def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=['start'])
async  def help_command(message: types.Message):
    await message.answer(text="Добро пожаловать в наш Телеграм Бот!")
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp)
