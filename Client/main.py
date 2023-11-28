import pika
def main():
    credentials = pika.PlainCredentials('mqadmin', 'Admin123XX_')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='send_email')
    channel.basic_publish(exchange='', routing_key='send_email', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()

if __name__ == '__main__':
    main()