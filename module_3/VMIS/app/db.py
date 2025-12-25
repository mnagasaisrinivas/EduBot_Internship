import sqlite3

def init_db():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_feedback(name, email, message):
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO feedback (name, email, message) VALUES (?, ?, ?)', (name, email, message))
    conn.commit()
    conn.close()

def get_all_feedback():
    conn = sqlite3.connect('feedback.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, email, message FROM feedback')
    results = cursor.fetchall()
    conn.close()
    return results
