from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

#Кнопка клавиатуры админа
button_1 = KeyboardButton('Женские деньги')
button_2 = KeyboardButton('Арканная чакрология')
button_3 = KeyboardButton('Курс Чакролог')
button_4 = KeyboardButton('Новогодний')

button_case_program = ReplyKeyboardMarkup(resize_keyboard=True).row(button_1, button_2).row(button_3, button_4)