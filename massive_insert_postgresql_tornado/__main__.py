"""Simple tornado demonstration app
"""

import tornado
import tornado.web

import psycopg2

from .insert_transaction_handler import InsertTransactionHandler
from .multiple_inserts_handler import MultipleInsertsHandler
from .copy_handler import CopyHandler

from .config import TORNADO_PORT

from .config import DB_NAME
from .config import DB_USER
from .config import DB_PASSWORD
from .config import DB_HOST

def main():
    """start the tornado server application
    """

    db = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
    )

    context = {
        "db": db,
    }

    application_tornado = tornado.web.Application(
        [
            (
                "/insert-transaction",
                InsertTransactionHandler,
                context
            ),
            (
                "/multiple-inserts",
                MultipleInsertsHandler,
                context
            ),
            (
                "/copy",
                CopyHandler,
                context
            ),
        ],
    )

    application_tornado.listen(
        TORNADO_PORT,
        decompress_request=True
    )

    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
