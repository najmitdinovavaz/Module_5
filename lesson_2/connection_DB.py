import psycopg2

con = psycopg2.connect(
    dbname="postgres",
    user='postgres',
    password='1',
    host='localhost',
    port=5432
)

cur = con.cursor()

user_table = """
    create table users(
        id serial primary key ,
        name varchar (255) ,
        age integer ,
        phone_number varchar (13) check (phone_number ilike '+%')
        )"""


# cur.execute(user_table)
# con.commit()


def user_save(name, age, phone_number):
    insert_query = """insert into users(name ,age , phone_number)
                    values (%s , %s , %s)"""
    params = (name, age, phone_number)

    cur.execute(insert_query, params)
    con.commit()


def user_list():
    select_user = """select * from users"""
    cur.execute(select_user)
    users = cur.fetchall()
    return users


# user_save("Avaz" , 17 , "+998339892206")
print(user_list())
