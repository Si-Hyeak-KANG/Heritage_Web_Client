# Flask 연결 위해 import
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# DB 연결 위해 항상 import하는 5줄
from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.fh0w7.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/heritage", methods=["POST"])
def web_heritage_post():
    ID_receive = request.form['ID_give']
    PW_receive = request.form['PW_give']
    Sector_receive = request.form['Sector_give']
    Title_receive = request.form['Title_give']
    Comment_receive = request.form['Comment_give']

    doc = {
        'ID': ID_receive,
        'PW' : PW_receive,
        'Sector' : Sector_receive,
        'Title' : Title_receive,
        'Comment' : Comment_receive

    }
    db.heritage.insert_one(doc)
    return jsonify({'msg': '글쓰기 완료!'})

@app.route("/heritage", methods=["GET"])
def web_heritage_get():
    allList = list(db.heritage.find({}, {'_id': False}))
    return jsonify({'lists': allList})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)