import sqlite3
import hashlib

# Initialize database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS orders (username TEXT, order_details TEXT)''')
    conn.commit()
    conn.close()

# Hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Authenticate user
def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()
    return result and result[0] == hash_password(password)

# Add user
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
    conn.commit()
    conn.close()