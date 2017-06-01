"""Handler that writes data with multiple inserts into a transaction
"""

import json
import tornado
import psycopg2
import psycopg2.extras

class InsertTransactionHandler(tornado.web.RequestHandler):

    def initialize(
        self,
        db,
    ):
        """Initializes the handler arguments.

        Args:
            db(psycopg2.extensions.connection) database connection
        """
        self.db = db

    def post(self):

        items = json.loads(self.request.body.decode("utf-8"))

        sql = "INSERT INTO items(message) VALUES "
        params = {}

        messages = items["messages"]
        amount = len(messages)

        for counter, item in enumerate(messages):
            key = "message_" + str(counter)

            sql += "(%(" + key + ")s)"
            if counter != amount - 1:
                sql += ","

            params[key] = item["message"]

        sql += ";"

        with self.db:
            with self.db.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:
                cursor.execute(
                    sql,
                    params
                )

        self.write("OK")
