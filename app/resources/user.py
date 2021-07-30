import json

from marshmallow import Schema, fields
from app.lib.validate_schema import validate
from app.models.user import UserModel, UserSchema


class UserPostSchema(Schema):
    name = fields.Str(required=True)
    fullname = fields.Str(required=True)


class UserResource:
    def on_get(self, req, resp, **params):
        users = self.db_session.query(UserModel).all()
        user_schema = UserSchema(many=True)
        res = user_schema.dump(users)
        resp.text = json.dumps(res)

    @validate(UserPostSchema)
    def on_post(self, req, resp, **params):
        data = req.context["request_data"]

        user = UserModel(name=data["name"], fullname=data["fullname"])
        result = self.db_session.add(user)

        self.db_session.commit()

        resp.text = f"Added user: {user}"
