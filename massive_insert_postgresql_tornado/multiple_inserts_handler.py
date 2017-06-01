"""Handler that writes data with multiple inserts
"""

import tornado
from tornado.web import gen

class MultipleInsertsHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("OK");
