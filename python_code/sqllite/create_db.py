import sqlite3

# sqlalchemy
# http://www.rmunn.com/sqlalchemy-tutorial/tutorial.html
# http://docs.sqlalchemy.org/en/latest/core/tutorial.html

def create_db():
    conn = sqlite3.connect('/home/pat/Documents/python_scripts/sqllite/example.db')

    c = conn.cursor()
    c.execute('''
              CREATE TABLE person
              (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
              ''')
    c.execute('''
              CREATE TABLE address
              (id INTEGER PRIMARY KEY ASC,
              street_name varchar(250),
              street_number varchar(250),
              post_code varchar(250) NOT NULL,
              person_id INTEGER NOT NULL,
               FOREIGN KEY(person_id) REFERENCES person(id))
              ''')

    c.execute('''
              INSERT INTO person VALUES(1, 'pythoncentral')
              ''')
    c.execute('''
              INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
              ''')
    conn.commit()
    conn.close()



def display_db():
    conn = sqlite3.connect('/home/pat/Documents/python_scripts/sqllite/example.db')
    res=[]
    c = conn.cursor()
    c.execute('SELECT * FROM person')
    res.append( c.fetchall())

    c.execute('SELECT * FROM address')
    res.append( c.fetchall())
    conn.close()
    return res

def Main():
    r=display_db()
    print r

if __name__=='__main__':
    Main()

