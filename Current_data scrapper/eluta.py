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
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer

def extract(query):
    url= "https://www.eluta.ca/rss?q=sort:rank+field:"
    query = query.replace(" ", "%20%")
    final_url = url + query
    print(final_url)
    url_xml = urlopen(final_url)
    xml = url_xml.read()
    url_xml.close()

    soup_page = BeautifulSoup(xml, "xml")
    list = soup_page.findAll("item")

    return create(list)
    
def create(list):
    L=[]
    for item in list:
        d={}
        d["title"]=item.title.text
        desc=item.description.text
        d["location"]=item.location.text
        d["date"]=item.pubDate.text
        d["link"]=item.link.text
        words=desc.split() #whitespace split
        words = [word.lower() for word in words] #to lower case
        table = str.maketrans('', '', string.punctuation) #remove punctuation marks
        strip = [w.translate(table) for w in words] #single words
        stop_words = set(stopwords.words('english')) #set of stopwords
        words = [w for w in strip if not w in stop_words] # remove stops words
        sentences = sent_tokenize(desc) #sentence formation
        d["keywords"]=words
        d["description"]=sentences
        L.append(d)
    return L