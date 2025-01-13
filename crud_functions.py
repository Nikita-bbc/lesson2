import sqlite3

connection = sqlite3.connect("database_1.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    title TEXT IF NOT NULL,
    description TEXT,
    price INTEGER IF NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT IF NOT NULL,
    age INTEGER IF NOT NULL,
    balance INTEGER IF NOT NULL,
    email TEXT IF NOT NULL
    );
    ''')


cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
               ('Таблетки для набора массы', 'Полезны', 100))
cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
               ('Таблетки для похудения', 'Полезны', 200))
cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
               ('Протеин', 'Полезно', 300))
cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
               ('Креатин', 'Полезно', 400))
connection.commit()


def get_all_products(id_product):
    product_list = cursor.execute("SELECT * FROM Products WHERE id = ?", (id_product, )).fetchone()
    return product_list


def add_user(username, email, age, balance=1000):
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username, )).fetchone()

    if check_user is None:
        cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
                       (username, email, age, balance))
    connection.commit()


def is_include(username):
    check_user = cursor.execute("SELECT * FROM Users WHERE username = ?", (username, )).fetchone()
    if check_user is None:
        return False
    else:
        return True


initiate_db()
connection.commit()
