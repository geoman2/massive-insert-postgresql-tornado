"""Handler that writes data with multiple inserts into a transaction
"""

import tornado
from tornado.web import gen

class InsertTransactionHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("OK");

