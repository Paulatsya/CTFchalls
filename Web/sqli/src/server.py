import os
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Get the absolute path of the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'vulnerable.db')

print(f"Permissions of vulnerable.db: {oct(os.stat('/home/ctf/vulnerable.db').st_mode)}")
# Create a simple SQLite database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    #c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    #c.execute("INSERT INTO users (username, password) VALUES ('admin', 'dscctf@dscctf8790')")
    #c.execute("INSERT INTO users (username, password) VALUES ('user', 'userpasspassuser@12345')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template_string('''
        <h1>Welcome to the CTF Challenge!</h1>
        <form action="/login" method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(query)
    user = c.fetchone()
    conn.close()
    flag = "dscctf{y0u_4r3_4n_5ql_4dm1n!}"

    if user:
        return render_template_string(f'<p>{flag}</p>')
    else:
        return "Invalid credentials!"

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=36088)
