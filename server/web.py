import tornado.ioloop
import tornado.web
import importlib as imp
import sys
import os

sys.path.append(os.path.dirname(__file__) + "/../compiler")
module = __import__('interpreter', fromlist=["make_choice"])
run = getattr(module, "run")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', result="", code="", data="")
    def post(self):

        code = self.get_argument('code')
        data = self.get_argument('input')
        result = str(run(code, data, "../compiler/pithon.core"))
        self.render('index.html', result=result, code=code, data=data)


routes = [
    (r"/", MainHandler),
    ('/images/(.*)', tornado.web.StaticFileHandler, {'path': 'images'}),
    ('/src-min-noconflict/(.*)', tornado.web.StaticFileHandler, {'path': 'src-min-noconflict'}),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()