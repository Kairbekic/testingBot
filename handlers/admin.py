from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from create_bot import dp, clientBot

ID = None
class FSMAdmin(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    country = State()
    city = State()

#Получаем ID текущего модератора
#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await clientBot.send_message(message.from_user.id, 'Что надо сделать, хозяин?', reply_markup=admin_kb.button_case_admin)
    await message.delete()

#Начало диалога загрузки нового пункта меню
#@dp.message_handler(commands='Загрузить', state=None)
async def cm_srart(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.first_name.set()
        await message.reply('Введите вашу фамилию')

#Выход из состояний
#@dp.message_handler(state="*", commands="отмена")
#@dp.message_handler(Text(equals='отмена',ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')

#Ловим первый ответ и пишем в словарь
#@dp.message_handler(content_types=['first_name'], state=FSMAdmin.first_name)
async def load_first_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['first_name'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите ваше имя")

#ловим второй ответ
#@dp.message_handler(state=FSMAdmin.last_name)
async def load_last_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['last_name'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите свой номер телефона")

#Ловим третий ответ
#@dp.message_handler(state=FSMAdmin.phone)
async def load_phone(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['phone'] = message.text
        await FSMAdmin.next()
        await message.reply("Укажите страну проживания")

#Ловим четвертый ответ
#@dp.message_handler(state=FSMAdmin.country)
async def load_country(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['country'] = message.text
        await FSMAdmin.next()
        await message.reply("Укажите город проживания")

# Ловим последний ответ и используем полученные данные
# @dp.message_handler(state=FSMAdmin.city)
async def load_city(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['city'] = message.text
        await sqlite_db.sql_add_command(state)
        await state.finish()

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)

@dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await clientBot.send_first_last_name(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
            await clientBot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().
                                         add(InlineKeyboardButton(f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))
#Выгрузка в ексель
async  def export_command(message: types.Message):
    await clientBot.send_message(message.from_user.id, 'test')

#Регистрируем хендлеры
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_srart, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(load_first_name, state=FSMAdmin.first_name)
    dp.register_message_handler(load_last_name, state=FSMAdmin.last_name)
    dp.register_message_handler(load_phone, state=FSMAdmin.phone)
    dp.register_message_handler(load_country, state=FSMAdmin.country)
    dp.register_message_handler(load_city, state=FSMAdmin.city)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(export_command, commands=['Выгрузить'])

