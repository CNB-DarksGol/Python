import sqlite3

connect = sqlite3.connect('user.db')

c = connect.cursor()

def Create_Table():
    c.execute('CREATE TABLE IF NOT EXISTS usuarios (User text, Password text)')

Create_Table() 

def Create_User():
    c.execute('INSERT INTO usuarios VALUES("root", "Senai132")')
    c.execute('INSERT INTO usuarios VALUES("teste", "Senai123")')
    connect.commit()
Create_User()
