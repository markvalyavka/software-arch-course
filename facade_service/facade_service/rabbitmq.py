import time

import pika

from facade_service.consul_api import c


class RabbitMqClient:

    def __init__(self):
        self._conn = None
        self._channel = None

    def init_app(self, app):
        print("Sleeping for 10 sec before MQ connection.")
        time.sleep(10)
        self._conn = pika.BlockingConnection(
             pika.ConnectionParameters(host=c.get_kv('RABBITMQ_URL'),
                                       port=5672)
        )
        self._channel = self._conn.channel()
        self.declare_queues()

    def declare_queues(self):
        self._channel.queue_declare(queue=c.get_kv('RABBITMQ_QUEUE_NAME'))

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
