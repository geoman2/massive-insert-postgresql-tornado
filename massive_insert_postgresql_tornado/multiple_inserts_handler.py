"""Handler that writes data with multiple inserts
"""

import tornado

class MultipleInsertsHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("OK");
