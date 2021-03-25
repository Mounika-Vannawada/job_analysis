import csv
import json
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def extract(query):
    url= "http://rss.jobsearch.monster.com/rssquery.ashx?q="
    query= "engineer"
    final_url = url + query
    url_xml = urlopen(final_url)
    xml = url_xml.read()
    url_xml.close()

    soup_page = BeautifulSoup(xml, "xml")
    list = soup_page.findAll("item")

    create(list)

def create(list):
    for item in list:
        print(item.title.text)
        a=item.description.text
        loc=a.split(",", 1)
        location=loc[0]
        print(location)
        desc=loc[1]
        words=desc.split() #whitespace split
        words = [word.lower() for word in words] #to lower case
        table = str.maketrans('', '', string.punctuation) #remove punctuation marks
        strip = [w.translate(table) for w in words] #single words
       
        sentences = sent_tokenize(desc)
        print(strip,"\n")
        print(sentences,"\n")

        tokens = word_tokenize(desc)
        words = [word for word in tokens if word.isalpha()]
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        print(words, "\n")
       
        port = PorterStemmer()
        stem = [port.stem(word) for word in tokens]
        print(stem, "\n")

query="engineer"
extract(query) 