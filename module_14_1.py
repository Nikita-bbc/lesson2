import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT IF NOT NULL,
email TEXT IF NOT NULL,
age INTEGER,
balance INTEGER IF NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}",

                                                                                             f"example{i}", 10 * i,
                                                                                             1000))
for j in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, j))

for k in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (k, ))

cursor.execute("SELECT * FROM Users WHERE age != ?", (60, ))
results = cursor.fetchall()
for elem in results:
    print(elem)

connection.commit()
connection.close()
