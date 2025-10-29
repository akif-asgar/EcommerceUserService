from celery import shared_task
import json
import pika
import os

@shared_task
def publish_user_created(user_id, email):
    
    RABBITMQ_URL = os.getenv('RABBITMQ_URL')
    if not RABBITMQ_URL:
        raise ValueError("RABBITMQ_URL not set in environment variables")

    params = pika.URLParameters(RABBITMQ_URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    # create fanout exchange 
    channel.exchange_declare(exchange='user.created', exchange_type='fanout')

    message = json.dumps({"user_id": user_id, "email": email})
    channel.basic_publish(exchange='user.created', routing_key='', body=message)
    connection.close()
