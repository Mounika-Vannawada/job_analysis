import pymongo
import re
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from json_parser import parser
import numpy as np
   
def query():
    client = pymongo.MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.zc1iw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    db  = client["mydatabase"]
    doc = db["historic"]

    dic = parser('../technologies.json')
    lang = [ [l, doc.find({"sector": l.lower()}).count() ] for l in dic['languages']]
    db = [ [l, doc.find({"sector": l.lower()}).count() ] for l in dic['Databases']]
    web = [ [l, doc.find({"sector": l.lower()}).count() ] for l in dic['Web Technologies']]
    devops = [ [l, doc.find({"sector": l.lower()}).count() ] for l in dic['DevOps Tools']]

    
    
query()
