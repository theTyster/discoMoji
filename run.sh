#! /usr/bin/env sh

main() {

python3 -m venv venv

. ./venv/bin/activate

pip install -r requirements.txt

rm emoji_urls.csv

./venv/bin/scrapy runspider ./code/discoMojo/spiders/emoji.py -o emoji_urls.csv:csv

mkdir ../scraped_emojis

rm ../scraped_emojis/*
wget --wait=1 -P ../scraped_emojis -i emoji_urls.csv
}

main
