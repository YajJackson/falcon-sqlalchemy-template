import falcon
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import skatebase.settings as settings
from skatebase.resources.image import Image
from skatebase.resources.user import UserResource
from skatebase.middleware.sqlalchemy import SQLAlchemySessionManager
from skatebase.middleware.logging import LogManager
from skatebase.middleware.marshmallow import SerializerMiddleware

engine = create_engine(
    "{engine}://{username}:{password}@{host}:{port}/{db_name}".format(
        **settings.POSTGRESQL
    )
)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

app = application = falcon.App(
    middleware=[
        SQLAlchemySessionManager(Session),
        LogManager(include_file=False),
        SerializerMiddleware()
    ]
)

app.add_route("/image", Image(storage_path="."))
app.add_route("/user", UserResource())
