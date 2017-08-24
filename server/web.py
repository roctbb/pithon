import tornado.ioloop
import tornado.web
import importlib as imp
import sys
import os
import markdown2

sys.path.append("../compiler")
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


class DocumentationHendler(tornado.web.RequestHandler):
    def get(self):
        with open('../README.md') as docs:
            html = markdown2.markdown(docs.read(), extras=["fenced-code-blocks", "break-on-newline", "tables"])
        self.render('documentation.html', html=html)

routes = [
    (r"/", MainHandler),
    (r"/documentation", DocumentationHendler),
    (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': 'images'}),
    (r'/src-min-noconflict/(.*)', tornado.web.StaticFileHandler, {'path': 'src-min-noconflict'}),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()