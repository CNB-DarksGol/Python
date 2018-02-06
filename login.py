import sqlite3

connect = sqlite3.connect('users.db')

c = connect.cursor()

passw = 'SELECT * FROM users WHERE Password = ?'
user = 'SELECT * FROM users WHERE User = ? and Password = ?'

def Ler_Dados(wordUsed):
    for row in c.execute(passw, (wordUsed,)):
        print row

    for row in c.execute(user, ('root', 'Senai132')):
        print row

Ler_Dados('')
