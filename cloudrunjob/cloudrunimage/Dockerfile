FROM python:3.10-slim

RUN echo "Cloud Run Dockerfile"

# ENV CRJ_DIR=/datasets/top/pipelines/CRJ_DIR

# ARG CONFIG_BUCKET

# COPY ${CRJ_CIR}/Pipfile* .

WORKDIR /app

COPY src /app/src

RUN apt-get -y update \
&& apt-get -y upgrade \
&& apt-get clean \
&& pip install pymysql

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

#gcloud sdk
# RUN curl -O "https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-449.0.0-linux-x86_64.tar.gz"
# RUN tar -xvf google-cloud-cli-449.0.0-linux-x86_64.tar.gz \
# && ./google-cloud-sdk/install.sh \
# && rm google-cloud-cli-449.0.0-linux-x86_64.tar.gz
# ENV  PATH="$PATH:/google-cloud-sdk/bin"
# RUN gsutil version

# COPY /datasets/top/pipelines/bq/ /bq/
# COPY ${CRJ_DIR}/src .

RUN addgroup --system --gid 1001 usergroup
RUN adduser --system --uid 1001 python

USER python

CMD ["python", "/app/src/main.py"]