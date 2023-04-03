
from aiogram import  types, Dispatcher
from create_bot import clientBot, dp
from keyboards import kb, ikb

HELP_COMMAND = """
/help - список команд
<b>/start</b> - <em>начать работу с ботом</em>
/description - что умеешь?
<b>❤️ give</b> - <em>стикер</em>
/links - ссылки
"""

#@dp.message_handler(commands=['help'])
async  def help_command(message: types.Message):
 #   await message.reply(text=HELP_COMMAND, parse_mode="HTML")
    await clientBot.send_message(chat_id=message.from_user.id,
                                 text=HELP_COMMAND,
                                 parse_mode="HTML")

#@dp.message_handler(commands=['start'])
async  def start_command(message: types.Message):
    await clientBot.send_message(chat_id=message.from_user.id,
                                 text="Добро пожаловать в наш Бот!",
                                 parse_mode="HTML",
                                 reply_markup=kb)
    await message.delete()

#@dp.message_handler(commands=['description'])
async  def desc_command(message: types.Message):
    await clientBot.send_message(chat_id=message.from_user.id,
                                 text="Наш бот умеет отправлять айди стикера")
    await message.delete()

#@dp.message_handler(commands=['give'])
async  def give_command(message: types.Message):
    await clientBot.send_sticker(message.from_user.id,
                                 sticker="CAACAgIAAxkBAAOBZCbC1uS62ivGg4ilivlO4NtYa_oAArsAAwku4BfvBsIRSARKDC8E")

#@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)

@dp.message_handler(commands=['links'])
async  def links_command(message: types.Message):
    await message.answer(text='Выберите опцию...',
                         reply_markup=ikb)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(help_command, commands='help')
    dp.register_message_handler(desc_command, commands=['description'])
    dp.register_message_handler(give_command, commands=['give'])
    dp.register_message_handler(send_sticker_id, commands='sticker')