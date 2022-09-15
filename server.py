import os

from flask import Flask
from tornado.ioloop import IOLoop
from tornado.web import Application, FallbackHandler
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer

from controllers import viewer


flask_app = Flask(
    __name__,
    template_folder=os.path.join(os.getcwd(), 'templates'),
)

flask_app.register_blueprint(viewer)


def start(port: int):
    flask_container = WSGIContainer(flask_app)
    app = Application(
        ([]) +
        [(r'.*', FallbackHandler, dict(fallback=flask_container))]
    )
    http_server = HTTPServer(app)
    http_server.listen(port=port)

    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()
        print('\nserver stopped')
    except Exception:
        IOLoop.current().stop()
        import traceback
        traceback.print_exc()



if __name__ == '__main__':
    start(8080)
