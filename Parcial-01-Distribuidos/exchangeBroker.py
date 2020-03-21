#! / usr / bin / env python
# -*- coding: utf-8 -*-
import pika
import time
#Hacemos la coneccion con el servidor
#Creamos el canal de comunicacion
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Declaramos el exchange, el cual va a administrar la cola hacia el consumidor 1
channel.exchange_declare(exchange='Group-One', exchange_type='fanout') # create a fanout pipe

#Declaramos el exchange, el cual va a administrar la cola hacia el consumidor 2
channel.exchange_declare(exchange='Group-Two', exchange_type='fanout') # create a fanout pipe

#Declaramos el exchange, el cual va a administrar la cola hacia ambos consumidore
channel.exchange_declare(exchange='Generally', exchange_type='fanout') # create a fanout pipe

for i in range(21):
    if i==7 or i==14 or i==21:
            channel.basic_publish(exchange='Generally', routing_key='', body='Hablando a los 2 consumidores')
            print(" [x] Sent 'Hablando a los 2 consumidores")
            time.sleep(2)
    else:
            if (i % 2 == 0):
                 channel.basic_publish(exchange='Group-One', routing_key='', body='Hablando con el consumidor 1, Msj:'+ str(i))
                 print(" [x] Sent 'Hablando con el consumidor 1")
                 time.sleep(2)
            else:
                 channel.basic_publish(exchange='Group-Two', routing_key='', body='Hablando con consumidor 2, Msj:'+ str(i))
                 print(" [x] Sent 'Hablando con consumidor 2")
                 time.sleep(2)

    
connection.close()