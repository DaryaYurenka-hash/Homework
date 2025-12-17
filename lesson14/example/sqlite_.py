import sqlite3
import os

WORK_DIR = os.path.dirname(__file__)

con = sqlite3.connect(os.path.join(WORK_DIR, 'db1.db'))
cursor = con.cursor()

sql = '''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT,
    lname TEXT,
    gender TEXT,
    age INTEGER NOT NULL);
'''

cursor.execute(sql)

sql = "INSERT INTO users (fname, lname, gender, age)  VALUES (?,?,?,?)"
cursor.execute(sql, ['Вася1', 'Васечкин1', 'm', 22])
cursor.execute(sql, ['Вася2', 'Васечкин2', 'm', 33])

sql = "SELECT * FROM users"
cursor.execute(sql)
data = cursor.fetchall()
print(data)


con.commit()
cursor.close()
con.close()