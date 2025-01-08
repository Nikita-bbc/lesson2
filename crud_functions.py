import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT IF NOT NULL,
    description TEXT,
    price INTEGER IF NOT NULL
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


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    res = cursor.fetchall()
    return res


