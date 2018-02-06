import sqlite3
import os
import getpass

connect = sqlite3.connect('users.db')

c = connect.cursor()

logger = ''
enter = ''

def LimpaTela():
   os.system('clear||cls')

LimpaTela()

try:
   LimpaTela()

   print('--- Menu ---\n')
   print('1) Criar usuario')
   print('2) Sistema de login')
   print('3) Todos usuarios\n')
   choose = int(raw_input('Escolha: '))

   if choose == 1:
       LimpaTela()
       print('--- Criar user no SQLite3 ---\n')
       Usuario = getpass.getuser(input('Login: '))
       Password = getpass.getpass('Senha: ')

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


   if choose == 2:
      LimpaTela()
      print('--- Sistema de Login SQLite3 ---\n')
      Usuario = str(raw_input('Login: '))
      Password = getpass.getpass('Password: ')

      login = 'SELECT * FROM users WHERE user = ? and password = ?'     

      def Ler_Dados():
          for row in c.execute(login,(Usuario, Password)):
              global logger
              logger = row[0]
              global enter
              enter = row[1]
      Ler_Dados()

      if Usuario == logger and Password == enter:
          print('Logado!')
      else:
          print('Erro ao logar!')
   
   if choose == 3:
      LimpaTela()
      print('--- Listagem de usuarios  ---')
      listar = 'SELECT * FROM users'
      
      def Listar_Users():
          for row in c.execute(listar):
              print(row[0])

      Listar_Users()
   
except (KeyboardInterrupt):
   print
