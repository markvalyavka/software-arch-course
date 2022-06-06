import sqlite3


class SqliteClient:

    def __init__(self):
        self._conn = None
        self._cur = None

    def init_app(self):
        self._conn = sqlite3.connect("messages.db", check_same_thread=False)
        self._cur = self._conn.cursor()
        self._cur.execute("create table if not exists messages (uuid, body)")

    def read_all_messages(self):
        messages = self._cur.execute("select * from messages").fetchall()
        return messages

    def insert_message(self, msg_w_uuid):
        self._cur.execute("insert into messages values (?, ?)",
                    (msg_w_uuid['uuid'], msg_w_uuid['message'])
        )
        self._conn.commit()

sqlite_db = SqliteClient()