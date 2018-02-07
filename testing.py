import sqlite3

connect = sqlite3.connect('users.db')

c = connect.cursor()

passw = 'SELECT * FROM users'

def Ler_Dados():
    for row in c.execute(passw):
        print row

Ler_Dados()
