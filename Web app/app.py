from flask import Flask, redirect, url_for, render_template, request, session
import json 
import pymongo
client = pymongo.MongoClient("mongodb+srv://gurpreet:gurpreet@cluster0.zc1iw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db  = client["mydatabase"]
mycol = db["currentData"]
app = Flask(__name__)
# -------- extract data and sent to frontend ---------------------------------------------------------- #

@app.route('/', methods=['GET', 'POST'])
def mainfun():
    d = { 'title':'Title', 'data' : 'dfdfdf' }
    l = [1,2,3,4,5]
    if request.method == "POST":
        req = request.form
        query = req.get('search')
        print("Post request with query: " + query)
        return render_template('index.html', data= d, list= l)
    return render_template('index.html', data= d, list= l)
       

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=5001)
