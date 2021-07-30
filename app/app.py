import falcon
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import app.settings as settings
from app.middleware.logging import LogManager
from app.middleware.sqlalchemy import SQLAlchemySessionManager
from app.resources.image import Image
from app.resources.user import UserResource

engine = create_engine(
    "{engine}://{username}:{password}@{host}:{port}/{db_name}".format(
        **settings.POSTGRESQL
    )
)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

app = application = falcon.App(
    middleware=[SQLAlchemySessionManager(Session), LogManager(include_file=False)]
)

app.add_route("/image", Image(storage_path="."))
app.add_route("/user", UserResource())
