import feedparser
import csv
import json
import pandas as pd

def extract(query):
    url= "http://rss.jobsearch.monster.com/rssquery.ashx?q="
    query= "engineer"
    final_url = url + query
    feed = feedparser.parse(final_url)
    b=feed["items"]
    create_csv(b)

def create_csv(b):
    for item in b:
        print(item["title"])
        print(item["link"])
        print(item["description"])

query="engineer"
extract(query)