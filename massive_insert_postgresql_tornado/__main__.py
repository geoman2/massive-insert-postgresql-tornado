"""Simple tornado demonstration app
"""

import tornado
import tornado.web

from .insert_transaction_handler import InsertTransactionHandler
from .multiple_inserts_handler import MultipleInsersHandler
from .copy_handler import CopyHandler

from .config import TORNADO_PORT

def main():
    """start the tornado server application
    """

    application_tornado = tornado.web.Application(
        [
            (r"/api", ApiHandler,),
        ],
    )
    application_tornado.listen(TORNADO_PORT, decompress_request=True)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
