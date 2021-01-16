FROM tiangolo/uvicorn-gunicorn:python3.8

COPY ./Pipfile Pipfile

RUN pip install pipenv && pipenv sync

COPY ./app /app