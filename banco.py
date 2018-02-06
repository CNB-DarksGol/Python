import sqlite3

connect = sqlite3.connect('users.db')

c = connect.cursor()

print('--- Criar user no SQLite3 ---')
Usuario = str(raw_input('Nome: '))
Password = str(raw_input('Senha: '))

def Create_Table():
    c.execute('CREATE TABLE IF NOT EXISTS users (user text, password text)')

def Create_User():
    c.execute('INSERT INTO users VALUES("{}", "{}")'.format(Usuario, Password))

if Usuario != None and Password != None:
   Create_Table()
   Create_User()
   connect.commit()
elif Usuario == None or Password == None:
   print('Tente novamente!')
else:
   print('Erro ao executar!')

