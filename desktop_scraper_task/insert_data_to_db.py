import sqlite3
import json
import os

def insert_data(data):
    conn = sqlite3.connect('computers.db')
    c = conn.cursor()
    for item in data:
        try:
            c.execute('''
                INSERT INTO computers (cpu_name, processor, motherboard, gpu, ram)
                VALUES (?, ?, ?, ?, ?)
            ''', (item['cpu_name'].strip(), 
                  item['processor'].strip(), 
                  item['motherboard'].strip(), 
                  item['gpu'].strip(), 
                  item['ram'].strip()))
            print(f"Inserted: {item}")
        except sqlite3.Error as e:
            print(f"Error for {item}: {e}")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'computers_data.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    insert_data(data)
