import pymongo
import re
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from json_parser import parser
import numpy as np


roles =["software", "database", "technicain", "architect", "manager", "engineer", "devops", "analyst", "web"]

def analysis2():
    client = pymongo.MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.zc1iw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    db  = client["mydatabase"]
    doc = db["currentDataNew"]

    contract = doc.find({"keywords": "contract"})
    fulltime = doc.find({"keywords": { '$all': ['full', 'time']}})

    con_vs_full = [['contract', contract.count()], ['fulltime', fulltime.count()]]\
    
    print(con_vs_full)

    role_job = {}
    for r in contract:
        for role in roles:
            if role in r['keywords']:
                role_job[role] = role_job.setdefault(role, 0) + 1

    print(role_job)
            
    role_job1 = {}
    for r in fulltime:
        for role in roles:
            if role in r['keywords']:
                role_job1[role] = role_job1.setdefault(role, 0) + 1

    print(role_job1)

analysis2()


 

    