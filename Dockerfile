FROM python:3.11
LABEL description='telegram bot'
WORKDIR /opt/app
COPY pyproject.toml poetry.lock README.md /opt/app/
RUN pip install poetry
RUN poetry install --no-root --no-interaction && \
    rm -rf ~/.cache/pypoetry
COPY ./storage ./storage
USER 1001:1001s 
CMD ["python","-m","storage"]