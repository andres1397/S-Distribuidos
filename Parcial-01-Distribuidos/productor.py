#! / usr / bin / env python
# -*- coding: utf-8 -*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Especificamos el canar, es decir, la cola
channel.queue_declare(queue='Grupo-01')

#Especificamos el Exchange donde va a ir, en este caso default
#Ademas el routing_key donde va el nombre de la cosa y el body con el contenido del mensaje
#El mensaje que se va a enviar es Hello-World

channel.basic_publish(exchange='',
                      routing_key='Grupo-01',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
