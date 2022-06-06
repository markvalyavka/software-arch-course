from multiprocessing import Process, Queue
import time

from messages_service.app import init_app
from consumer import mq_consumer
from messages_service.sqllite import sqlite_db

app = init_app()
mq_consumer.init_app()
sqlite_db.init_app()

if __name__ == "__main__":

    # start consumer in a new process
    thread = Process(target=mq_consumer.start_consuming)
    thread.start()
    app.run(debug=True, host="0.0.0.0", port=5003)
