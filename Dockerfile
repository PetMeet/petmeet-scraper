FROM ubuntu:18.04

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "python3", "python3-pip"]
RUN ["pip3", "install", "scrapy"]
RUN ["pip3", "install", "pika"]

COPY . .

ENV SPIDER="protectora_lugo_spider"

# Just for testing
# ENTRYPOINT ["/bin/bash", "-c", "python3 -m unittest discover"]
# Testing and spider
ENTRYPOINT ["/bin/bash", "-c", "python3 -m unittest discover && scrapy crawl $SPIDER"]