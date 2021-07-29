import json

from falcon import HTTP_OK, HTTPBadRequest, HTTPNotFound, HTTPUnprocessableEntity
from skatebase.models.user import User as _User


class User:
    def on_get(self, req, resp, **params):
        users = ["user1", "user2"]
        resp.text = json.dumps(users)
