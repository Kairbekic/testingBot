from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
from gsheet import GoogleSheet

def main():
    gs = GoogleSheet()
    test_range = 'TestList!A1:D20'
    test_values = sqlite_db.myfunc()
    gs.updateRangeValues(test_range, test_values)

async def on_startup(_):
    print('Бот был успешно запущен!')
    sqlite_db.sql_start()
    main()


from handlers import client, other, admin

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
