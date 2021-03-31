import pymongo
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from json_parser import parser
import numpy as np
import re
   
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
    graphdict['contract'] = contract
    graphdict['fulltime'] = fulltime
    return(graphdict)




def analysis2():
    client = pymongo.MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.zc1iw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    db  = client["mydatabase"]
    doc = db["historic"]

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

    labels = ['experienced' ,'manager',  'entry level']
    year_max = [  max(exp['year']) ,max(manager['year']),  max(entry['year']) ]
    year_min = [ min(exp['year']),  min(manager['year']),  min(entry['year'])]
    hour_max = [  max(exp['hours']),  max(manager['hours']),  max(entry['hours'])]
    hour_min = [  min(exp['hours']),  min(manager['hours']), min(entry['hours'])]

    
    dict1 = {'labels': labels, 'yearmax' : year_max , 'yearmin' : year_min, 'hourmax' : hour_max , 'hourmin' : hour_min}
  
    return(dict1)
    
    
    
def salary(sal):
    cur  = re.compile(r"\d{1,3}(?:,\d{3})*(?:\.\d+)?(?=\s)")  
    sal = cur.findall(sal)[-1] if cur.findall(sal) else '0.00'
    sal = int(sal.split(".")[0].replace(",", ""))
    return sal


def analysis3():
    
    roles =["software", "database", "technicain", "architect", "manager", "engineer", "devops", "analyst", "web"]
    client = pymongo.MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.zc1iw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db  = client["mydatabase"]
    doc = db["currentDataNew"]
    contract = doc.find({"keywords": "contract"})
    fulltime = doc.find({"keywords": { '$all': ['full', 'time']}})
    con_vs_full = {'contract': contract.count(), 'fulltime': fulltime.count()}
    role_job = {}
    for r in contract:
        for role in roles:
            if role in r['keywords']:
                role_job[role] = role_job.setdefault(role, 0) + 1
    
            
    role_job1 = {}
    for r in fulltime:
        for role in roles:
            if role in r['keywords']:
                role_job1[role] = role_job1.setdefault(role, 0) + 1 
    dict1 = {'conVsFull' : con_vs_full, 'roles' : roles,'jobkey' : list(role_job.keys()),'jobkey1' : list(role_job1.keys()), 'roleJob': list(role_job.values()) , 'roleJob1' : list(role_job1.values())}
    print(dict1)
    return(dict1)
runQuery()
