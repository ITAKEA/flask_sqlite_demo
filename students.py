import sqlite3

def create():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER, name TEXT)")
        cur.execute("INSERT INTO students VALUES(1, 'Claus')")
        cur.execute("INSERT INTO students VALUES(2, 'Pia')")
        cur.execute("INSERT INTO students VALUES(3, 'Hans')")
        return None


def read():

    stundents = []
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")

        for i in cur.fetchall():
            stundents.append(i)
        
        return stundents