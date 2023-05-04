"""

MATHEUS DE SOUZA MELO
2019007565
SISTEMAS DISTRIBUIDOS

"""

import pika
import psutil
import time

# Produtor
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declara a fila
channel.queue_declare(queue='cpu_queue')
channel.queue_declare(queue='incendios_queue')

#Consumidor 1
def callback(ch, method, properties, body):
    cpu_temp = float(body.split()[2].strip('°C'))
    if cpu_temp > 70:
        channel.basic_publish(exchange='incendios', routing_key='detectado', body='Fogo detectado!')
        channel.basic_publish(exchange='prevencao', routing_key='ativar', body='Ativar sistema de prevenção!')

#Consumidor 2
def callback_alarm(ch, method, properties, body):
    print('Perigo, finge que tem um alarme  pra incendio tocando!!!')

channel.basic_consume(queue='cpu_queue', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='incendios_queue', on_message_callback=callback_alarm, auto_ack=True)

while True:

    cpu_temp = psutil.sensors_temperatures().get('cpu-thermal', [])[0].current
    message = f'Temperatura da CPU: {cpu_temp} em °C'
    channel.basic_publish(exchange='temperaturas', routing_key='cpu', body=message)
    time.sleep(1)

