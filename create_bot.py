from aiogram import Bot, Dispatcher
from config import TOKEN_API

clientBot = Bot(TOKEN_API)
dp = Dispatcher(clientBot)