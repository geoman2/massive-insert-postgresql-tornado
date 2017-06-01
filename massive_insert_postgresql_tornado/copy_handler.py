"""Handler that use the psycopg2 copy method
"""

import json
import psycopg2
import psycopg2.extras
from io import StringIO
import tornado

class CopyHandler(tornado.web.RequestHandler):

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

        values = ""
        for item in items["messages"]:
            values += item["message"] + "\n"

        with self.db:
            with self.db.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:
                cursor.copy_from(
                    StringIO(values),
                    "items",
                    columns=('message',)
                )

        self.write("OK");
