from aiogram import Bot, Dispatcher
from config import TOKEN_API
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
clientBot = Bot(TOKEN_API)
dp = Dispatcher(clientBot, storage=storage)

