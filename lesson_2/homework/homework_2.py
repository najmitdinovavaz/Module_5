import psycopg2
import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart

con = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    host='localhost',
    password='1',
    port=5432
)

cur = con.cursor()
con.commit()

start_table = """
    create table users_information(
        id serial primary key , 
        user_id bigint ,
        user_name varchar (255 ) unique not null ,
        first_name varchar (255) ,
        last_name varchar (255) ,
        created_at timestamp default current_timestamp 
        )"""

cur.execute(start_table)
con.commit()


def save_db(user_id, user_name, first_name, last_name):
    query = "select * from users_information where user_id = %s"
    cur.execute(query, (user_id,))
    user = cur.fetchone()

    if user:
        print("User already exists in the database.")
    else:
        queries = """
        insert into users_information (user_id , user_name , first_name , last_name)
        values (%s,%s,%s,%s)
        """

        params = (user_id, user_name, first_name, last_name)

        cur.execute(queries, params)
        con.commit()
        print("User information saved to the database.")


BOT_TOKEN = "6327601579:AAFLGqXY3beXxerfQ9qIg-vjzibEjgIg_tw"
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    await message.answer(f"{user_name} Your information has been saved to the database",
                         reply_markup=save_db(user_id, user_name, first_name, last_name))


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
