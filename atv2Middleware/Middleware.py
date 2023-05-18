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


# Consumidor 1 - Verificação de temperatura da CPU
def callback(ch, method, properties, body):
    # Obtém as temperaturas da CPU
    temperatures = psutil.sensors_temperatures().get('cpu-thermal', [])
    
    if temperatures:
        # Obtém a temperatura atual da CPU
        cpu_temp = temperatures[0].current
        
        if cpu_temp > 70:
            # Se a temperatura estiver acima de 70°C, publica mensagens em duas exchanges diferentes
            channel.basic_publish(exchange='incendios', routing_key='detectado', body='Fogo detectado!')
            channel.basic_publish(exchange='prevencao', routing_key='ativar', body='Ativar sistema de prevenção!')
    else:
        # Caso a temperatura da CPU não esteja disponível
        print('A temperatura da CPU não está disponível.')


# Consumidor 2 - Simulação de alarme de incêndio
def callback_alarm(ch, method, properties, body):
    print('Perigo, finge que tem um alarme de incêndio tocando!!!')


channel.basic_consume(queue='cpu_queue', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='incendios_queue', on_message_callback=callback_alarm, auto_ack=True)

# Produtor de temperaturas
while True:
    # Obtém as temperaturas da CPU
    temperatures = psutil.sensors_temperatures().get('cpu-thermal', [])
    
    if temperatures:
        # Obtém a temperatura atual da CPU
        cpu_temp = temperatures[0].current
        
        # Cria a mensagem com a temperatura da CPU
        message = f'Temperatura da CPU: {cpu_temp} em °C'
        print(message)
        
        # Publica a mensagem na exchange 'temperaturas' com a rota 'cpu'
        channel.basic_publish(exchange='temperaturas', routing_key='cpu', body=message)
    else:
        # Caso a temperatura da CPU não esteja disponível
        message = 'A temperatura da CPU não está disponível.'
        print(message)
        
        # Publica a mensagem na exchange 'temperaturas' com a rota 'cpu'
        channel.basic_publish(exchange='temperaturas', routing_key='cpu', body=message)
    
    # Aguarda 1 segundo antes de obter a próxima temperatura
    time.sleep(1)

# Inicia o consumidor
channel.start_consuming()

