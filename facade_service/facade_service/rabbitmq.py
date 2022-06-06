import pika
import time


class RabbitMqClient:

    def __init__(self):
        self._conn = None
        self._channel = None

    def init_app(self, app):
        print("Sleeping for 5 sec before MQ connection.")
        time.sleep(5)
        self._conn = pika.BlockingConnection(
             pika.ConnectionParameters(host=app.config['RABBITMQ_URL'],
                                       port=5672)
        )
        self._channel = self._conn.channel()
        self.declare_queues()

    def declare_queues(self):
        self._channel.queue_declare(queue='msgs')

    @property
    def channel(self):
        return self._channel

    def publish_msg(self, rk, msg_body, exchange=''):
        self._channel.basic_publish(
            exchange=exchange,
            routing_key=rk,
            body=msg_body
        )
        print(f"Sent {msg_body}")


mq = RabbitMqClient()
