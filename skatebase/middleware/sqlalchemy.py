from sqlalchemy.orm import scoped_session


class SQLAlchemySessionManager:
    """
    Create a scoped session for every request and close it when the request
    ends.
    """

    def __init__(self, Session: scoped_session):
        self._Session = Session

    def process_resource(self, req, resp, resource, params):
        resource.db_session = self._Session()

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, "db_session"):
            self._Session.remove()
