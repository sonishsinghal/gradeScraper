from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
from utils.Scraper import scraper
import os

client = MongoClient("mongodb+srv://ayush:x1AfIua2Dfebz8LE@cluster0.nvule.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["scraper"]
col = db["data"]
dataset={
    "username":"ce20b022",
    "html":"<h1>demo htlm</h1>"
}
col.insert_one(dataset)

app:Flask = Flask(__name__)
CORS(app)

@app.route("/scrape", methods=['POST'])
def scrapeRoute()->str:
    rollNumber:str = None
    password:str = None
    data:str = None
    try:
        rollNumber = str(request.json["rollnumber"])
        password = str(request.json["password"])
        data = scraper(rollNumber, password)
    except KeyError:
        return "Roll Number or Password not Found"
    except Exception:
        return "Internal server error"
    return data

@app.route("/",methods=['GET'])
def route()->str:
    content:str = None
    try:
        file = open("./index.html", 'r')
        content = file.read()
        file.close()
    except Exception as e:
        return str(e)
    return content
    
if(__name__ == "__main__"):
    app.run(debug=True)