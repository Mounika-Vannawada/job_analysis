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

    contract = doc.find({"sector": "contract"}).count()
    fulltime = doc.find({"sector": { '$all': ['full', 'time']}}).count()
    
    d = doc.find( { 'salary': {'$ne': np.nan}})
    
    exp = {'hours': [], 'year': [], 'total': 0}
    manager = {'hours': [], 'year': [], 'total': 0}

    entry =  {'hours': [], 'year': [], 'total': 0}
    for v in d:
        if 'experienced' in v['sector'] and 'nonmanager' in v['sector']:
            exp['total'] += 1
            salary1 = salary(v['salary'])
            if salary1 < 10:
                pass
            elif salary1 <200:
                exp['hours'].append(salary1)
            elif salary1 < 40000:
                pass
            else:
                exp['year'].append(salary1)
        if 'manager' in v['sector']:
            manager['total'] += 1
            salary2 = salary(v['salary'])
            if salary2 < 10:
                pass
            elif salary2 <200:
                manager['hours'].append(salary2)
            elif salary2 < 70000:
                pass
            else:
                manager['year'].append(salary2)
        if 'entry' in v['sector'] and 'level' in v['sector']:
            entry['total'] += 1
            salary3 = salary(v['salary'])
            if salary3 < 10:
                pass
            elif salary3 <200:
                entry['hours'].append(salary3)
            elif salary3 < 30000:
                pass
            else:
                entry['year'].append(salary3)
    
    print(max(exp['hours']), min(exp['year']), max(exp['year']))
     
    print(max(manager['hours']), min(manager['year']), max(manager['year']))

    print(max(entry['hours']), min(entry['year']), max(entry['year']))
    print(exp['total'], manager['total'], entry['total'])

    
def salary(sal):
    cur  = re.compile(r"\d{1,3}(?:,\d{3})*(?:\.\d+)?(?=\s)")  
    sal = cur.findall(sal)[-1] if cur.findall(sal) else '0.00'
    sal = int(sal.split(".")[0].replace(",", ""))
    return sal

query()
