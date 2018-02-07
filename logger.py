import sqlite3
import paho.mqtt.client as mqtt
import os
import time
import getpass

mqttc = mqtt.Client()
mqttc.connect("127.0.0.1", 80, 60)

connect = sqlite3.connect('users.db')

c = connect.cursor()

CHORANDO = 'START'
logger = ''
enter = ''

def TestConnection():
    if True:
       print('\nConectado!')
    else:
       print('Erro ao conectar.')
       time.sleep(1.5)
       print('Reconectando..')
       mqttc.reconnect()

def LimpaTela():
    os.system('clear||cls')

def Ler_Dados():
    for row in c.execute(login,(Usuario, Password)):
        global logger
        logger = row[0]
        global enter
        enter = row[1]


while CHORANDO != 'STOP':
    LimpaTela()
    print('--- Sistema de Login SQLite3 ---\n')
    Usuario = str(raw_input('Login: '))
    Password = getpass.getpass('Password: ')

    login = 'SELECT * FROM users WHERE user = ? and password = ?'

    Ler_Dados()

    if Usuario == logger and Password == enter:
        CHORANDO = 'STOP'
        if True:
            TestConnection()
    else:
        print('\nErro ao logar!')
        time.sleep(1.5)
