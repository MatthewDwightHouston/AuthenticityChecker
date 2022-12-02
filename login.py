import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

username = request.form['username']
password = request.form['password']

# Create table
c.execute('''CREATE TABLE users
             (username text, password text)''')

# Insert a row