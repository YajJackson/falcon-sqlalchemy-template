import falcon.asgi
from tortoise import run_async

from skatebase.database import startDB
from skatebase.resources.image import Image
from skatebase.resources.user import User


def create_app(config=None):
    # await startDB()

    app = application = falcon.asgi.App()

    print('add routes to app')
    app.add_route("/image", Image(storage_path="."))
    app.add_route("/user", User())

    return app
