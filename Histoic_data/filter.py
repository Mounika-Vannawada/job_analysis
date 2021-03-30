import pandas as pd
import csv
import string
import nltk
nltk.download('punkt')
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
import pymongo
client = pymongo.MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.zc1iw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def read(f):
    count = 0 
    col=["job_title","date_added","job_type","job_description","location","page_url","salary","sector"]
    df1 = pd.read_csv(f,sep=',', usecols=col, encoding='latin-1')  
    df1.astype(str)
    L=[]
    for row in df1.itertuples(index=True, name='Pandas'):
         d={}
         d["title"]=row.job_title
         d["date"]=row.date_added
         d["type"]=row.job_type
         d["location"]=row.location
         d["link"]=row.page_url
         d["salary"]=row.salary
         s=row.job_description
         sentences = sent_tokenize(s) #sentence formation
         l=str(row.sector)
         words=l.split(' ') #whitespace split
         words = [word.lower() for word in words] #to lower case
         table = str.maketrans('', '', string.punctuation) #remove punctuation marks
         strip = [w.translate(table) for w in words] #single words
         stop_words = set(stopwords.words('english')) #set of stopwords
         words = [w for w in strip if not w in stop_words] # remove stops words"""
         d["sector"]= words
         d["description"]= sentences
         #L.append(d)
         count += 1
         saverecord(d)
         
    return count


def saverecord(mydict):
    db  = client["mydatabase"]
    mycol = db["historic"]
    print(mycol.insert_one(mydict))

#to save data in the mongodb database
# ======== Main ============================================================== #
if __name__ == "__main__":
    #this is demo file combined2.csv
    count = read('C://Users//gurpr//Desktop//fall assignment//winter assignments//Database//project//github//job_analysis//Histoic_data//combined2.csv')
    print(count + " records of historic data inserted successfully in the mongo atlas database")