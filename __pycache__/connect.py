import pymongo
client = pymongo.MongoClient("mongodb+srv://amrit:amrit@cluster0.uszj7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["mydatabase"]
mycol = db["customers"]
mydict = {"first": "amrit", "last" : "dhaliwal"}
mycol.insert_one(mydict)