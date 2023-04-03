from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button_help = KeyboardButton('/help')
button_description = KeyboardButton('/description')
button_give = KeyboardButton('/give')
button_links = KeyboardButton('/links')
kb_client.add(button_help).insert(button_description).row(button_links, button_give)

ikb_client = InlineKeyboardMarkup(row_width=2)
ikb1 = InlineKeyboardButton(text='Apple',
                            url="www.apple.com")
ikb2 = InlineKeyboardButton(text='Google',
                            url="www.google.com")
ikb_client.add(ikb1).insert(ikb2)