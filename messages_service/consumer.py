import json
import time

import pika

import config as cfg

from messages_service.sqllite import sqlite_db


class RabbitMqClient:

    def __init__(self):
        self._conn = None
        self._channel = None

    def init_app(self):
        print("Sleeping for 10 sec before MQ connection.")
        time.sleep(10)
        self._conn = pika.BlockingConnection(
             pika.ConnectionParameters(
                 host=cfg.DebugConfig.RABBITMQ_URL
             )
        )
        self._channel = self._conn.channel()
        self.declare_queues()

    def declare_queues(self):
        self._channel.queue_declare(queue='msgs')

    @property
    def channel(self):
        return self._channel

    @staticmethod
    def msg_recv_callback(ch, method, properties, body):
        msg = json.loads(body)
        print(" [x] Received %r" % msg)
        sqlite_db.insert_message(msg)


    def start_consuming(self):

        self._channel.basic_consume(
            queue='msgs',
            on_message_callback=RabbitMqClient.msg_recv_callback,
            auto_ack=True
        )
        self._channel.start_consuming()


mq_consumer = RabbitMqClient()
