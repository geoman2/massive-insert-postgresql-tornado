"""Handler that use the psycopg2 copy method
"""

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
        self.write("OK");
