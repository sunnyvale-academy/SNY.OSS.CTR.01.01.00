import pika
import os 

def send_message(queue_name: str, message: str):
    # Connect to RabbitMQ (default on localhost:5672)
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

    while True:
        # Send the message
        channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2  # make message persistent
            )
        )
        print(f" [x] Sent '{message}' to queue '{queue_name}'")

    

    # Close connection
    connection.close()


if __name__ == "__main__":
    # Example usage
    send_message("test_queue", "Hello RabbitMQ!")