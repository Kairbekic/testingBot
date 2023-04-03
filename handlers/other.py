from aiogram import types, Dispatcher
from create_bot import dp
#@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply(message.text + ' ❤️')

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(send_emoji)