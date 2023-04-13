from aiogram import  types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import clientBot, dp
from keyboards import client_kb
from keyboards import program_kb
from data_base import sqlite_db
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

#@dp.message_handler(commands=['start','help'])
async  def start_command(message: types.Message):
    try:
        await clientBot.send_message(chat_id=message.from_user.id, text="Добро пожаловать!", reply_markup=client_kb.button_case_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/assistant_chakrologist_bot')

#@dp.message_handler(commands=['Режим работы'])
async  def pizza_open_command(message: types.Message):
    await clientBot.send_message(chat_id=message.from_user.id, text="Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00")

#@dp.message_handler(commands=['Расположение'])
async  def pizza_place_command(message: types.Message):
    await clientBot.send_message(message.from_user.id, 'Без адреса')

class FSMClient(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    country = State()
    city = State()
    program_name = State()
    user_id = State()

#Начало диалога загрузки нового пункта меню
#@dp.message_handler(commands='Загрузить', state=None)
async def cm_srart(message: types.Message):
    await clientBot.send_message(message.from_user.id, 'Прошу пройти небольшую регистрацию',
                                 reply_markup=client_kb.button_case_client)
    await FSMClient.first_name.set()
    await clientBot.send_message(message.from_user.id, "Введите вашу фамилию")

#Выход из состояний
#@dp.message_handler(state="*", commands="отмена")
#@dp.message_handler(Text(equals='отмена',ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Регистрация отменена')

#Ловим первый ответ и пишем в словарь
#@dp.message_handler(content_types=['first_name'], state=FSMAdmin.first_name)
async def load_first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await FSMClient.next()
    await clientBot.send_message(message.from_user.id, "Введите ваше имя")

#ловим второй ответ
#@dp.message_handler(state=FSMAdmin.last_name)
async def load_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await FSMClient.next()
    await clientBot.send_message(message.from_user.id, "Введите свой номер телефона")

#Ловим третий ответ
#@dp.message_handler(state=FSMAdmin.phone)
async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await FSMClient.next()
    await clientBot.send_message(message.from_user.id, "Укажите страну проживания")

#Ловим четвертый ответ
#@dp.message_handler(state=FSMAdmin.country)
async def load_country(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['country'] = message.text
    await FSMClient.next()
    await clientBot.send_message(message.from_user.id, "Укажите город проживания")

# Ловим последний ответ и используем полученные данные
# @dp.message_handler(state=FSMAdmin.city)
async def load_city(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['city'] = message.text
        await FSMClient.next()
        await clientBot.send_message(message.from_user.id, "Укажите курс", reply_markup=program_kb.button_case_program)

async def load_program_name(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['program_name'] = message.text
            data['user_id'] = message.from_user.id
        await sqlite_db.sql_add_command(state)
        await state.finish()
        await clientBot.send_message(message.from_user.id, 'Регистрация окончена, спасибо', reply_markup = client_kb.button_case_client)


#Регистрируем хендлеры
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands='Режим_работы')
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(cm_srart, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_first_name, state=FSMClient.first_name)
    dp.register_message_handler(load_last_name, state=FSMClient.last_name)
    dp.register_message_handler(load_phone, state=FSMClient.phone)
    dp.register_message_handler(load_country, state=FSMClient.country)
    dp.register_message_handler(load_city, state=FSMClient.city)
    dp.register_message_handler(load_program_name, state=FSMClient.program_name)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
