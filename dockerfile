FROM python:3.9

WORKDIR /app

COPY skatebase .
COPY pyproject.toml .


ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD ["./startup.sh"]