from flask import Flask, render_template, jsonify, request, Request
import sqlite3
import os
from datetime import date as d

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

def get_today(date: str | None = None) -> str:
    return d.today().isoformat() if not date else date


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET', 'POST', 'DELETE'])
def data():
    if request.method == 'GET':
        with get_db_connection() as conn:
            today = get_today(request.args.get('date'))
            total_intake = conn.execute('SELECT SUM(amount) FROM water_intake WHERE date = ?', (today,)).fetchone()[0]
        return jsonify({'total_intake': total_intake or 0})
    elif request.method == 'POST':
        data = request.get_json()
        amount = data.get('amount')
        today = get_today(data.get('date'))
        with get_db_connection() as conn:
            conn.execute('INSERT INTO water_intake (date, amount) VALUES (?, ?)', (today, amount))
            conn.commit()
        return jsonify({'status': 'success'})
    elif request.method == 'DELETE':
        data = request.get_json()
        today = get_today(data.get('date'))
        with get_db_connection() as conn:
            conn.execute('DELETE FROM water_intake WHERE date = ?', (today,))
            conn.commit()
        return jsonify({'status': 'success'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)