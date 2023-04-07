import sqlite3 as sq
from create_bot import clientBot
#import pandas as pd

#filePath = 'C:\Users\kairbekov_m\Desktop\myEx.xlsx'
def sql_start():
    global base, cur
    base = sq.connect('chacrology.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS Users(FirstName TEXT, LastName TEXT PRIMARY KEY, Phone TEXT, Country TEXT, City TEXT)')
    base.commit()

def myfunc():
    test_values = [
        ["Фамилия", "Имя", "Номер телефона", "Страна", "Город"],
    ]
    testList = list()
    for ret in cur.execute("SELECT * FROM Users").fetchall():
        test_values.append(ret)
    return test_values

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO Users VALUES (?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM Users').fetchall():
        await clientBot.send_message(message.from_user.id, f'\nФамилия: {ret[0]}\nИмя: {ret[1]}\nТелефон: {ret[2]}\nСтрана: {ret[3]}\nГород {ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM Users').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM Users WHERE LastName == ?', (data,))
    base.commit()