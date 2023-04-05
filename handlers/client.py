from aiogram import  types, Dispatcher
from create_bot import clientBot, dp
from keyboards import kb_client, ikb_client
from data_base import sqlite_db

#@dp.message_handler(commands=['start','help'])
async  def start_command(message: types.Message):
    try:
        await clientBot.send_message(chat_id=message.from_user.id, text="Приятного аппетита!", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/assistant_chakrologist_bot')

#@dp.message_handler(commands=['Режим работы'])
async  def pizza_open_command(message: types.Message):
    await clientBot.send_message(chat_id=message.from_user.id, text="Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00")

#@dp.message_handler(commands=['Расположение'])
async  def pizza_place_command(message: types.Message):
    await clientBot.send_message(message.from_user.id, 'ул. Толстого 8')

@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


#Регистрируем хендлеры
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands='Режим_работы')
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])
