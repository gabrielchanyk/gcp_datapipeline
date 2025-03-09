FROM python:3.10-slim

RUN echo "Cloud Run Dockerfile"

WORKDIR /app

COPY src /app/src

COPY src/yaml_sql /app/yaml_sql

RUN apt-get -y update \
&& apt-get -y upgrade \
&& apt-get clean

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN addgroup --system --gid 1001 usergroup
RUN adduser --system --uid 1001 python

USER python

CMD ["python", "/app/src/main.py"]