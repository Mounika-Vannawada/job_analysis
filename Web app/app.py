from flask import Flask, redirect, url_for, render_template, request, session
import json 
import pymongo
client = pymongo.MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.zc1iw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db  = client["mydatabase"]
mycol = db["currentData"]
import query

app = Flask(__name__)
# -------- extract data and sent to frontend ---------------------------------------------------------- #

@app.route('/', methods=['GET', 'POST'])
def mainfun():
    '''
    if request.method == "POST":
        req = request.form
        query = req.get('search')
        print("Post request with query: " + query)
    '''
    graphDict = query.runQuery()
    pie = {'Contract' : graphDict['contract'], 'fulltime' :graphDict['fulltime'] }

    return render_template('index.html', graph1= graphDict['lang'], graph2= graphDict['db'], pie = pie)
# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=5001)
