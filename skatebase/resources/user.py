import json

from falcon import HTTP_OK, HTTPBadRequest, HTTPNotFound, HTTPUnprocessableEntity
from skatebase.models.user import UserModel


class UserResource:
    def on_get(self, req, resp, **params):
        self.logger.info(f"User table: {UserModel.__tablename__}")
        users = ["user1", "user2"]
        resp.text = json.dumps(users)
