from pymongo import MongoClient
from flask import request
import pymongo
import datetime
import certifi
uri="mongodb+srv://navya19mehta:navya_m@cluster0.ke9vcjg.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
db=client["database1"]

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('BootstrapExample.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        dictionary=db.test.find_one({"key4":"student"})
        n=dictionary["key1"]
        p=dictionary["key4"]
        cursor=db.students.find()
        documents=[
            {
                'name':'Milk',
                'price':4.00,
                'quantity':3,
            },
            {
                'name':'Watermelon',
                'price':2.00,
                'quantity':2,
            },
            {
                'name':'Apple',
                'price':1.00,
                'quantity':5,
            }
        ]
        return render_template('flaskform.html',n=n,p=p,documents=documents)
    if request.method=='POST':
        name=request.form["first-name"]
        age=request.form["age"]
        city=request.form["city"]
        profession=request.form["profession"]
        document={"key1":name,"key2":age,"key3":city,"key4":profession}
        document1={
            'name': 'Mickey Mouse',
            'age' : 10,
            'grade': 5,
            'parents': ['Mr. Mouse', 'Mrs. Mouse'],
            'scores': {
                'math': 89,
                'science': 95,
                'english': 92},
                'timestamp': datetime.datetime.utcnow()
                }
        document2={
            'name': 'Minnie Mouse',
            'age' : 11,
            'grade': 6,
            'parents': ['Mr. Mouse', 'Mrs. Mouse'],
            'scores': {
                'math': 89,
                'science': 99,
                'english': 67},
                'timestamp': datetime.datetime.utcnow()
                }
        db.test.insert_one(document)
        db.test.insert_many([document1,document2])
        return render_template('flaskform.html')
if __name__=="__main__":
    app.debug=True
    app.run()