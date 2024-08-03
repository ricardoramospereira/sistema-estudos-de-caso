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

def listar_estudos():
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, titulo FROM estudos')
    estudos = [{'id': row[0], 'titulo': row[1]} for row in cursor.fetchall()]
    conn.close()
    return estudos

def listar_passos(titulo_estudo):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT passos.id, passos.passo, passos.problema 
                      FROM passos
                      JOIN estudos ON estudos.id = passos.estudo_id
                      WHERE estudos.titulo = ?''', (titulo_estudo,))
    passos = [{'id': row[0], 'passo': row[1], 'problema': row[2]} for row in cursor.fetchall()]
    conn.close()
    return passos

def obter_estudo_id_por_titulo(titulo):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM estudos WHERE titulo = ?', (titulo,))
    estudo_id = cursor.fetchone()[0]
    conn.close()
    return estudo_id

def excluir_passo(passo_id):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM passos WHERE id = ?', (passo_id,))
    conn.commit()
    conn.close()

def excluir_todos_passos(estudo_id):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM passos WHERE estudo_id = ?', (estudo_id,))
    conn.commit()
    conn.close()

def excluir_estudo(estudo_id):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    # Primeiro, exclua todos os passos associados
    excluir_todos_passos(estudo_id)
    # Agora, exclua o estudo de caso
    cursor.execute('DELETE FROM estudos WHERE id = ?', (estudo_id,))
    conn.commit()
    conn.close()

def estudo_existe(titulo):
    conn = sqlite3.connect('estudos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM estudos WHERE LOWER(titulo) = LOWER(?)', (titulo,))
    existe = cursor.fetchone()[0] > 0
    conn.close()
    return existe