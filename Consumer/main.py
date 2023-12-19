import pika
import smtplib

def main():
    credentials = pika.PlainCredentials('mqadmin', 'Admin123XX_')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='send_email', durable=True)
    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        enviar_email(body.decode())
    channel.basic_consume(queue='send_email', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def enviar_email(message: str):
    sender = 'ppcantalice121@gmail.com'
    password = 'luvsxfongxfzpwvz'
    receivers = ['pedrothegamer2@gmail.com']
    message = """From: ppcantalice121@gmail.com
    Subject: Prontuario do Paciente


    Prontuario feito pelo HospitalCare
    Obrigado pela Preferencia
    """

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com: 587')
        smtpObj.starttls()
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, message)         
        print("Successfully sent email")
    except Exception as e:
        print(e)
        pass
