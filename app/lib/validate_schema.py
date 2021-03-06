from functools import wraps

import falcon
import falcon.status_codes as status
from marshmallow import Schema, ValidationError
from app.lib.errors import HTTPError


# https://falcon.readthedocs.io/en/stable/_modules/falcon/media/validators/jsonschema.html
# TODO: response validation
# TODO: async validation
def validate(req_schema: Schema = None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, req, resp, *args, **kwargs):
            if req_schema is not None:
                request_data = {}

                try:
                    request_data |= req.params | req.media
                except:
                    pass

                try:
                    req.context["request_data"] = req_schema().load(data=request_data)
                except ValidationError as err:
                    raise HTTPError(status=status.HTTP_422, errors=err.messages)

            result = func(self, req, resp, *args, **kwargs)

            return result

        return wrapper

    return decorator
