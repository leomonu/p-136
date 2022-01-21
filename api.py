from flask import Flask, json,jsonify,request
from flask import Flask,jsonify,request

from starsData import data

app  = Flask(__name__)
@app.route("/")
def getdata():
    return jsonify({
        "data":data,
        "msg":"Success"
    })
@app.route("/stars")
def stars():
    name = request.args.get("Name")
    starData = next(i for i in data if i["Name"]== name)
    return jsonify({"data":starData,"msg":"Success"})
    
if(__name__ == "__main__"):
    app.run(debug = True,port = 5000)