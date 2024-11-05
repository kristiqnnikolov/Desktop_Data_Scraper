from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

print(" * LINK TO DATA: http://127.0.0.1:5000/computers")

def query_database(processor=None, gpu=None, motherboard=None, ram=None):
    conn = sqlite3.connect('computers.db')
    c = conn.cursor()
    query = 'SELECT id, cpu_name, processor, motherboard, gpu, ram FROM computers WHERE 1=1'
    params = []
    
    if processor:
        query += ' AND processor LIKE ?'
        params.append(f'%{processor}%')
    if gpu:
        query += ' AND gpu LIKE ?'
        params.append(f'%{gpu}%')
    if motherboard:
        query += ' AND motherboard LIKE ?'
        params.append(f'%{motherboard}%')
    if ram:
        query += ' AND ram LIKE ?'
        params.append(f'%{ram}%')
    
    c.execute(query, params)
    results = c.fetchall()
    conn.close()

    return [{'id': row[0], 'cpu_name': row[1], 'processor': row[2], 'motherboard': row[3], 'gpu': row[4], 'ram': row[5]} for row in results]

@app.route('/computers', methods=['GET'])
def get_computers():
    processor = request.args.get('processor')
    gpu = request.args.get('gpu')
    motherboard = request.args.get('motherboard')
    ram = request.args.get('ram')
    
    filtered_data = query_database(processor, gpu, motherboard, ram)

    return jsonify(filtered_data), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True)

