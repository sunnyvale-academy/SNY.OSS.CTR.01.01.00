import pika
import os

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    # Acknowledge message
    ch.basic_ack(delivery_tag=method.delivery_tag)

def receive_messages(queue_name: str):
    # Connect to RabbitMQ (default on localhost:5672)
    credentials = pika.PlainCredentials(
        os.environ['RABBITMQ_USERNAME'], 
        os.environ['RABBITMQ_PASSWORD']
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.environ['RABBITMQ_HOST'], 
            port=os.environ['RABBITMQ_PORT'],
            credentials = credentials
        )
    )

    channel = connection.channel()

    # Make sure the queue exists
    channel.queue_declare(queue=queue_name, durable=True)

    # Fair dispatch: don't give more than one message at a time to a worker
    channel.basic_qos(prefetch_count=1)

    # Subscribe to the queue
    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback
    )

    print(f" [*] Waiting for messages in '{queue_name}'.")
    channel.start_consuming()

if __name__ == "__main__":
    receive_messages("test_queue")