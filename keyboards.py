from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('/help')
button2 = KeyboardButton('/description')
button3 = KeyboardButton('❤️ give')
kb.add(button1).insert(button2).add(button3)

ikb = InlineKeyboardMarkup(row_width=2)
ikb1 = InlineKeyboardButton(text='Apple',
                            url="www.apple.com")
ikb2 = InlineKeyboardButton(text='Google',
                            url="www.google.com")
ikb.add(ikb1).insert(ikb2)