FROM python:3.10-slim-bullseye

LABEL maintainer="Abhishek Vaish <abhishek.vaish@acsicorp.com>"

WORKDIR /blog-app/src

COPY ./pyproject.toml /blog-app/
COPY ./poetry.lock /blog-app/

RUN python3 -m pip install poetry  \
    && poetry config virtualenvs.create false  \
    && poetry install

COPY ./src .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]