from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue dans le challenge d'injection SQL basique. Essayez de trouver les utilisateurs."

@app.route('/users')
def users():
    user_id = request.args.get('id')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        users = cursor.execute(query).fetchall()
        return str(users)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
