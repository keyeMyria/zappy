FROM python:3.6

ENV PYTHONBUFFERED 1

# pull and install requirements first in order to cache them
COPY ./requirements /requirements

RUN pip install -r /requirements/production.txt \
    && groupadd -r django \
    && useradd -r -g django django


COPY . /app
RUN chown -R django /app

COPY ./gunicorn.sh /gunicorn.sh
COPY ./gunicorn_config.py /gunicorn_config.py

RUN sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /gunicorn.sh \
    && chown django:django /gunicorn.sh \
    && chown django:django /gunicorn_config.py

WORKDIR /app

EXPOSE 5000

CMD ["/gunicorn.sh"]
