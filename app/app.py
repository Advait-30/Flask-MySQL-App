

import os
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configuration from environment variables
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "flaskdb")
MYSQL_USER = os.environ.get("MYSQL_USER", "flaskuser")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "flaskpass")

def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        database=MYSQL_DATABASE,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD
    )

@app.route('/')
def index():
    return "Hello from Flask with MySQL!"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')
            cursor.execute('INSERT INTO users (name) VALUES (%s)', (name,))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'message': 'User added', 'name': name}), 201
        except Error as e:
            return jsonify({'error': str(e)}), 500
    else:
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute('CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))')
            cursor.execute('SELECT * FROM users')
            users = cursor.fetchall()
            cursor.close()
            conn.close()
            return jsonify(users)
        except Error as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)