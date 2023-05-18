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

# Declara a exchange
channel.exchange_declare(exchange='temperaturas', exchange_type='direct')


# Consumidor 1
def callback(ch, method, properties, body):
    temperatures = psutil.sensors_temperatures().get('cpu-thermal', [])
    if temperatures:
        cpu_temp = temperatures[0].current
        if cpu_temp > 70:
            channel.basic_publish(exchange='incendios', routing_key='detectado', body='Fogo detectado!')
            channel.basic_publish(exchange='prevencao', routing_key='ativar', body='Ativar sistema de prevenção!')
    else:
        print('A temperatura da CPU não está disponível.')


# Consumidor 2
def callback_alarm(ch, method, properties, body):
    print('Perigo, finge que tem um alarme de incêndio tocando!!!')


channel.basic_consume(queue='cpu_queue', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='incendios_queue', on_message_callback=callback_alarm, auto_ack=True)


while True:
    temperatures = psutil.sensors_temperatures().get('cpu-thermal', [])
    if temperatures:
        cpu_temp = temperatures[0].current
        message = f'Temperatura da CPU: {cpu_temp} em °C'
        print(message)
        channel.basic_publish(exchange='temperaturas', routing_key='cpu', body=message)
    else:
        message = 'A temperatura da CPU não está disponível.'
        print(message)
        channel.basic_publish(exchange='temperaturas', routing_key='cpu', body=message)
    time.sleep(1)

# Inicie o consumidor
channel.start_consuming()

