from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

#Кнопка клавиатуры админа
button_load = KeyboardButton('/Добавить')
button_delete = KeyboardButton('/Удалить')
button_menu = KeyboardButton('/Список')
button_export = KeyboardButton('/Выгрузить')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).row(button_load, button_menu).row(button_export, button_delete)