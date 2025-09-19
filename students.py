import sqlite3

def create():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
        cur.execute("INSERT INTO students (name) VALUES(?)", ('Claus',))
        cur.execute("INSERT INTO students (name) VALUES('Pia')")
        cur.execute("INSERT INTO students (name) VALUES('Hans')")
        return None


def read_all():

    stundents = []
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")

        for i in cur.fetchall():
            stundents.append(i)
        
        return stundents