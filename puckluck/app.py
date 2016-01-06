
import os.path

import momoko
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from puckluck.handlers import *

define("port", default=8888, help="run on the given port", type=int)

db_database = os.environ.get('PUCKLUCK_DB', 'puckluck')
db_user = os.environ.get('PUCKLUCK_USER', 'postgres')
db_password = os.environ.get('PUCKLUCK_PASSWORD', '')
db_host = os.environ.get('PUCKLUCK_HOST', '')
db_port = os.environ.get('PUCKLUCK_PORT', 5432)
dsn = 'dbname={} user={} password={} host={} port={}'.format(
        db_database, db_user, db_password, db_host, db_port)

assert (db_database or db_user or db_password or db_host or db_port) is not None, (
    'Environment variables for the examples are not set. Please set the following '
    'variables: PUCKLUCK_DB, PUCKLUCK_USER, PUCKLUCK_PASSWORD, '
    'PUCKLUCK_HOST, PUCKLUCK_PORT')


def main():
    try:
        tornado.options.parse_command_line()
        handlers = [
            (r'/', MainHandler)
        ]
        settings = dict(
                debug=True,
                template_path=os.path.join(os.path.dirname(__file__), "templates"),
                static_path=os.path.join(os.path.dirname(__file__), "static")
        )
        app = tornado.web.Application(handlers, **settings)

        ioloop = tornado.ioloop.IOLoop.instance()

        app.db = momoko.Pool(
                dsn=dsn,
                size=1,
                max_size=3,
                ioloop=ioloop,
                setsession=("SET TIME ZONE UTC",),
                raise_connect_errors=False
        )

        future = app.db.connect()
        ioloop.add_future(future, lambda f: ioloop.stop())
        ioloop.start()

        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        ioloop.start()
    except KeyboardInterrupt:
        print('Exit.')


if __name__ == '__main__':
    main()
