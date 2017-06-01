"""Handler that writes data with multiple inserts
"""

import json
import tornado
import psycopg2
import psycopg2.extras

class MultipleInsertsHandler(tornado.web.RequestHandler):

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

        with self.db:
            with self.db.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor
            ) as cursor:

                for item in items["messages"]:
                    cursor.execute(
                        """
                        INSERT INTO items (
                            message
                        ) VALUES (
                            %(message)s
                        );
                        """,
                        {
                            "message": item["message"]
                        }
                    )

        self.write("OK");
