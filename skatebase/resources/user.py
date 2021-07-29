import json

from falcon import HTTP_OK, HTTPBadRequest, HTTPNotFound, HTTPUnprocessableEntity
from skatebase.models.user import UserModel
from marshmallow import fields, Schema


class UserPostSchema(Schema):
    name = fields.Str(required=True)
    fullname = fields.Str(required=True)


class UserResource:
    serializers = {
        "post": UserPostSchema,
    }

    def on_get(self, req, resp, **params):
        self.logger.info(f"User table: {UserModel.__tablename__}")
        users = ["user1", "user2"]
        resp.text = json.dumps(users)

    def on_post(self, req, resp, **params):
        data = req.context["serialized_data"]

        user = UserModel(name=data["name"], fullname=data["fullname"])
        result = self.db_session.add(user)

        self.db_session.commit()

        resp.text = f"Added user: {user}"
