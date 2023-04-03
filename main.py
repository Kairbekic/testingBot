from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config import TOKEN_API
from keyboards import kb, ikb

import string
import random

HELP_COMMAND = """
/help - список команд
<b>/start</b> - <em>начать работу с ботом</em>
/description - что умеешь?
<b>❤️ give</b> - <em>стикер</em>
/links - ссылки
"""
clientBot = Bot(TOKEN_API)
dp = Dispatcher(clientBot)

async def on_startup(_):
    print('Бот был успешно запущен!')

@dp.message_handler(commands=['help'])
async  def help_command(message: types.Message):
 #   await message.reply(text=HELP_COMMAND, parse_mode="HTML")
    await clientBot.send_message(chat_id=message.from_user.id,
                                 text=HELP_COMMAND,
                                 parse_mode="HTML")

@dp.message_handler(commands=['start'])
async  def start_command(message: types.Message):
    await clientBot.send_message(chat_id=message.from_user.id,
                                 text="Добро пожаловать в наш Бот!",
                                 parse_mode="HTML",
                                 reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['description'])
async  def desc_command(message: types.Message):
    await clientBot.send_message(chat_id=message.from_user.id,
                                 text="Наш бот умеет отправлять айди стикера")
    await message.delete()

@dp.message_handler(commands=['give'])
async  def give_command(message: types.Message):
    await clientBot.send_sticker(message.from_user.id,
                                 sticker="CAACAgIAAxkBAAOBZCbC1uS62ivGg4ilivlO4NtYa_oAArsAAwku4BfvBsIRSARKDC8E")

@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)

@dp.message_handler(commands=['links'])
async  def links_command(message: types.Message):
    await message.answer(text='Выберите опцию...',
                         reply_markup=ikb)

@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply(message.text + ' ❤️')

if __name__ == '__main__':
    executor.start_polling(dp,
                           on_startup=on_startup,
                           skip_updates=True)
