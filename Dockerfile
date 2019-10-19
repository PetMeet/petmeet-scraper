FROM ubuntu:18.04

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "python3", "python3-pip"]
RUN ["pip3", "install", "scrapy"]
RUN ["pip3", "install", "pika"]

RUN ["scrapy", "-v"]

COPY . .

ENTRYPOINT ["scrapy", "crawl", "protectora_lugo_spider"]