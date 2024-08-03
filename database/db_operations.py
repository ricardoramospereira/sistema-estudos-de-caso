import sqlite3

def adicionar_estudo(titulo):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO estudos (titulo) VALUES (?)', (titulo,))
    conn.commit()
    conn.close()

def adicionar_passo(estudo_id, passo, problema):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passos (estudo_id, passo, problema, resolvido) VALUES (?, ?, ?, 0)', 
                   (estudo_id, passo, problema))
    conn.commit()
    conn.close()
