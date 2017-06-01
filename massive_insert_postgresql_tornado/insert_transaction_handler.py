"""Handler that writes data with multiple inserts into a transaction
"""

import tornado
from tornado.web import gen

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
        self.write("OK");
