import sqlite3

def init_db():
    conn = sqlite3.connect('computers.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS computers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpu_name TEXT NOT NULL,
            processor TEXT NOT NULL,
            motherboard TEXT NOT NULL,
            gpu TEXT NOT NULL,
            ram TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
