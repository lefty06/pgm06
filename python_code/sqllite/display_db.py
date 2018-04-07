import sqlite3

conn = sqlite3.connect('/home/pat/Documents/python_scripts/sqllite/example.db')

c = conn.cursor()
c.execute('SELECT * FROM person')
print c.fetchall()
c.execute('SELECT * FROM address')
print c.fetchall()
conn.close()
