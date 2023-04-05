from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_open = KeyboardButton('/Режим_работы')
button_place = KeyboardButton('/Расположение')
button_menu = KeyboardButton('/Меню')

kb_client.row(button_open, button_place).add( button_menu)

ikb_client = InlineKeyboardMarkup(row_width=2)
ikb1 = InlineKeyboardButton(text='Apple',
                            url="www.apple.com")
ikb2 = InlineKeyboardButton(text='Google',
                            url="www.google.com")
ikb_client.add(ikb1).insert(ikb2)