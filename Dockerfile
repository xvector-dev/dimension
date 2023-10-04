FROM python:3.9

RUN apt update && apt install nginx -y && \
    apt-get update && \
    apt-get install build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

COPY . .

RUN pip install -r requirements.txt

WORKDIR /singularity-api
COPY run.sh .

RUN chmod +x run.sh


CMD ["./run.sh"]