import json

from marshmallow import Schema, fields
from skatebase.lib.validate_schema import validate
from skatebase.models.user import UserModel


class UserPostSchema(Schema):
    name = fields.Str(required=True)
    fullname = fields.Str(required=True)


class UserResource:
    def on_get(self, req, resp, **params):
        users = ["user1", "user2"]

        self.logger.info(
            f"User table: {UserModel.__tablename__} has {len(users)} users."
        )

        resp.text = json.dumps(users)

    @validate(UserPostSchema)
    def on_post(self, req, resp, **params):
        data = req.context["request_data"]

        user = UserModel(name=data["name"], fullname=data["fullname"])
        result = self.db_session.add(user)

        self.db_session.commit()

        resp.text = f"Added user: {user}"
