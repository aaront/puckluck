import tornado.web
from tornado import gen


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.render('index.html')
