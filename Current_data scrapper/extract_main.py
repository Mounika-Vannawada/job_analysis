import eluta
import indeed 
import monster
import pymongo
client = pymongo.MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.zc1iw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


roles =["Software Developer","Software Engineer","Software Tester","Software Engineering Intern",
"Software Quality Assurance Specialist","Software Programmer","Web Developer","Database Engineer",
"Software QA Tester","Software Test Engineer","Data Analyst","Business Analyst","DevOps","C","C++",
"Python","Java","Testing","AWS","Azure","computer","Node.js","Backend","frontend","Developer",
"Android","Swift"]

def saverecord(mydict):
    db  = client["mydatabase"]
    mycol = db["currentData"]
    print(mycol.insert_one(mydict))

if __name__=="__main__":
    
    for role in roles: 
        print(role)
        L =eluta.extract(role)
        for dict1 in L:
            if isinstance(dict1, dict):
                print("eluta")
                saverecord(dict1)
        L =indeed.extract(role)
        for dict1 in L:
            if isinstance(dict1, dict):
                print("indeed")
                saverecord(dict1)
      
        L = monster.extract(role)
        for dict1 in L:
            if isinstance(dict1, dict):
                print("mosnter")
                saverecord(dict1)
                
        print("saved")
    