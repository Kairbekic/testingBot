from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

#Кнопка клавиатуры админа
button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')
button_export = KeyboardButton('/Выгрузить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).row(button_export, button_delete)