import paho.mqtt.client as mqtt
import time

# Trazendo resposta se houve exito ao conectar. 
def TestConnection():
    if True:
       print('Conectado!')
    else:
       print('Erro ao conectar.')
       time.sleep(2)
       print('Reconectando..')
       mqttc.reconnect()

mqttc = mqtt.Client()
mqttc.connect("127.0.0.1", 80, 60)

TestConnection()

mqttc.loop_forever()
