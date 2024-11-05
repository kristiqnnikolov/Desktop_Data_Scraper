import sqlite3

def verify_data():
    conn = sqlite3.connect('computers.db')
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM computers')
    count = c.fetchone()[0]
    conn.close()
    print(f"Total entries in database: {count}")

if __name__ == "__main__":
    verify_data()
