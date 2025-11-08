from flask import Flask, render_template, jsonify, request
import sqlite3
import os

app = Flask(__name__)

# Database setup
def get_db_connection():
    conn = sqlite3.connect('data/user_data.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if os.path.exists('data/user_data.db'):
        return
    conn = get_db_connection()
    conn.execute('CREATE TABLE water_intake (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL, amount INTEGER NOT NULL)')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    today = request.args.get('date')
    if not today:
        from datetime import date
        today = date.today().isoformat()
    
    total_intake = conn.execute('SELECT SUM(amount) FROM water_intake WHERE date = ?', (today,)).fetchone()[0]
    conn.close()
    
    return jsonify({'total_intake': total_intake or 0})

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.get_json()
    amount = data.get('amount')
    today = data.get('date')
    if not today:
        from datetime import date
        today = date.today().isoformat()

    conn = get_db_connection()
    conn.execute('INSERT INTO water_intake (date, amount) VALUES (?, ?)', (today, amount))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success'})

@app.route('/api/data', methods=['DELETE'])
def reset_data():
    data = request.get_json()
    today = data.get('date')
    if not today:
        from datetime import date
        today = date.today().isoformat()

    conn = get_db_connection()
    conn.execute('DELETE FROM water_intake WHERE date = ?', (today,))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)