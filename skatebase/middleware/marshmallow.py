# Inspired by https://eshlox.net/2017/08/02/falcon-framework-request-data-validation-serializer-middleware-marshmallow

import falcon.status_codes as status
from skatebase.lib.errors import HTTPError

from marshmallow import ValidationError


class SerializerMiddleware:
    def process_resource(self, req, resp, resource, params):
        request_data = {}
        request_data |= req.params
        try:
            request_data |= req.media
        except:
            pass

        try:
            request_data |= req.context.get("request")
        except:
            pass

        try:
            serializer = resource.serializers[req.method.lower()]
        except (AttributeError, IndexError, KeyError):
            return
        else:
            try:
                req.context["serialized_data"] = serializer().load(data=request_data)
            except ValidationError as err:
                raise HTTPError(status=status.HTTP_422, errors=err.messages)
