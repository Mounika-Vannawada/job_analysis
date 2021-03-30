import pymongo
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from json_parser import parser
   
def runQuery():
    graphdict = {}
    client = pymongo.MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.zc1iw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db  = client["mydatabase"]
    doc = db["historic"]

    dic = parser('./technologies.json')
    lang = [ [l, doc.find({"sector": l.lower()}).count() ] for l in dic['languages']]
    db = [ [l, doc.find({"sector": l.lower()}).count() ] for l in dic['Databases']]
    web = [ [l, doc.find({"sector": l.lower()}).count() ] for l in dic['Web Technologies']]
    devops = [ [l, doc.find({"sector": l.lower()}).count() ] for l in dic['DevOps Tools']]

    contract = doc.find({"sector": "contract"}).count()
    fulltime = doc.find({"sector": { '$all': ['full', 'time']}}).count()

    graphdict['lang'] = lang
    graphdict['db'] = db
    graphdict['web'] = web
    graphdict['devops']= devops
    print("contract")
    print( contract)
    print(fulltime)
    graphdict['contract'] = contract
    graphdict['fulltime'] = fulltime
    return(graphdict)
runQuery()
