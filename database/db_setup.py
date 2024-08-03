import sqlite3

def init_db():
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS estudos (
                        id INTEGER PRIMARY KEY,
                        titulo TEXT
                      )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS passos (
                        id INTEGER PRIMARY KEY,
                        estudo_id INTEGER,
                        passo TEXT,
                        problema TEXT,
                        resolvido INTEGER,
                        FOREIGN KEY (estudo_id) REFERENCES estudos(id)
                      )''')
    conn.commit()
    conn.close()
