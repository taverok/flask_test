FROM python:3.5-slim

RUN mkdir /app
WORKDIR /app
ADD . /app/

ENV DEBIAN_FRONTEND=noninteractive \
    FLASK_APP=/app/app.py \
    FLASK_DEBUG=1 \
    PYTHONPATH="${PYTHONPATH}:/usr/lib/python3/dist-packages/"

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && apt-get install -y default-libmysqlclient-dev \
                          mysql-client \
                          python3-libtorrent \
                          supervisor \
                          redis-tools \
                          less \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    # supervisor
    && ln -s /app/instance/supervisor.conf /etc/supervisor/conf.d

EXPOSE 8000
ENTRYPOINT ["/app/instance/entrypoint.sh"]