import sqlite3

# função para criar o banco de dados
def listar_estudos():
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, titulo FROM estudos')
    estudos = [{'id': row[0], 'titulo': row[1]} for row in cursor.fetchall()]
    conn.close()
    return estudos

# função para listar os passos de um estudo
def listar_passos(titulo_estudo):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT passos.passo, passos.problema 
                      FROM passos
                      JOIN estudos ON estudos.id = passos.estudo_id
                      WHERE estudos.titulo = ?''', (titulo_estudo,))
    passos = [{'passo': row[0], 'problema': row[1]} for row in cursor.fetchall()]
    conn.close()
    return passos

# função para adicionar um novo estudo
def adicionar_estudo(titulo):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO estudos (titulo) VALUES (?)', (titulo,))
    conn.commit()
    conn.close()

# função para adicionar um novo passo
def adicionar_passo(estudo_id, passo, problema):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passos (estudo_id, passo, problema, resolvido) VALUES (?, ?, ?, 0)', 
                   (estudo_id, passo, problema))
    conn.commit()
    conn.close()
