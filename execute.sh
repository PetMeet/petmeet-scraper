#!/bin/bash

# Perform spider tests
python3 -m unittest discover

# Execute all spiders
for spider in $(scrapy list)
do
  scrapy crawl $spider
done
