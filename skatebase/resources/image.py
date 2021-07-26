import io
import json
import mimetypes
import os
import uuid

import falcon


class Image:

    _CHUNK_SIZE_BYTES = 4096

    # The resource object must now be initialized with a path used during POST
    def __init__(self, storage_path):
        self._storage_path = storage_path

    async def on_get(self, req, resp):
        doc = {"images": [{"href": "/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png"}]}

        # Create a JSON representation of the resource
        resp.text = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200

    async def on_post(self, req, resp):
        ext = mimetypes.guess_extension(req.content_type)
        name = f"{uuid.uuid4()}{ext}"
        image_path = os.path.join(self._storage_path, name)

        with io.open(image_path, "wb") as image_file:
            while True:
                chunk = req.stream.read(self._CHUNK_SIZE_BYTES)
                if not chunk:
                    break

                image_file.write(chunk)

        resp.status = falcon.HTTP_201
        resp.location = "/images/" + name


class ImageStore:

    _CHUNK_SIZE_BYTES = 4096

    # Note the use of dependency injection for standard library
    # methods. We'll use these later to avoid monkey-patching.
    def __init__(self, storage_path, uuidgen=uuid.uuid4, fopen=io.open):
        self._storage_path = storage_path
        self._uuidgen = uuidgen
        self._fopen = fopen

    def save(self, image_stream, image_content_type):
        ext = mimetypes.guess_extension(image_content_type)
        name = f"{uuid.uuid4()}{ext}"
        image_path = os.path.join(self._storage_path, name)

        with self._fopen(image_path, "wb") as image_file:
            while True:
                chunk = image_stream.read(self._CHUNK_SIZE_BYTES)
                if not chunk:
                    break

                image_file.write(chunk)

        return name
