# Python Falcon SQA Template

## Features

- [Falcon](https://falcon.readthedocs.io/en/stable/) rest api framework
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/) modelling
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) integration with support for auto generated migrations
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) schema definition / request validation
- [Poetry](https://python-poetry.org/docs/) dependency management

## Requirements

- Docker Compose (Docker) [installation instructions](https://docs.docker.com/compose/install/)

## Getting started

- Run `docker-compose up --build` (You should see `db` and `api` services start.)

# Development notes

## Migrations

After adding a new model to `app/models/` you will need to include the appropriate import line to `migrations/env.py` so that alembic has a reference to the updated table metadata. More about this can be found [here](https://github.com/sqlalchemy/alembic/issues/712).

Example

```python
...

from app.models.model import Base
from app.models.user import UserModel
from app.models.<your-model> import <your-model> # <-- Add this line

target_metadata = Base.metadata

...
```

You should then be able to generate a new alembic migration via executing `alembic revision --autogenerate -m "Add Example Table"` inside the api container.
