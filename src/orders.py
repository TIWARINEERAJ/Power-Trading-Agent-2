import sqlite3

def cancel_order(order_id):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("DELETE FROM orders WHERE rowid = ?", (order_id,))
    conn.commit()
    conn.close()

def list_orders(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT rowid, order_details FROM orders WHERE username = ?", (username,))
    orders = c.fetchall()
    conn.close()
    return orders