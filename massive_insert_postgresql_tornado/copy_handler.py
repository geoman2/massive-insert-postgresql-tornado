"""Handler that use the psycopg2 copy method
"""

import tornado
from tornado.web import gen

class CopyHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("OK");
