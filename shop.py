from pymongo import MongoClient
from flask import request
import pymongo
import certifi
uri="mongodb+srv://navya19mehta:_database1_@cluster0.by8g6ao.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
db=client["database1"]
from flask import Flask, render_template
from flask import *
import os
cart=[]
STATIC_FOLDER = 'static'

app=Flask(__name__)
id=0
app.config['STATIC_FOLDER'] = STATIC_FOLDER

app.secret_key = 'super secret key'

cart={}
items=1

@app.route('/',methods=['GET','POST'])
def index():
    global id
    flash('')
    products=db.products.find()
    shops=db.shop_users.find()
    if request.method=='POST':
        if 'test1' in request.form:
            print(2, request.form)
            shopname=request.form["shopname"]
            ownername=request.form["ownername"]
            email=request.form["email"]
            contact=request.form["contact"]
            password=request.form["password"]
            id+=1
            document={
                    'Shop Name' : shopname,
                    'Owner Name' : ownername,
                    'Email': email,
                    'Contact' : contact,
                    'Password' : password,
                    'ID' : str(id)
            }
            c=id
            db.shop_users.insert_one(document)
            return render_template('index.html',shops=shops,products=products)
        elif 'test2' in request.form:
            loginemail=request.form['loginemail']
            loginpassword=request.form['loginpassword']
            i=db.shop_users.find_one({"Email":loginemail})
            if i!=None and i['Email']==loginemail:
                if loginpassword==i['Password']:
                    flash('Successful login')
                    return redirect('/owner-home')
                else:
                    flash('Incorrect password.')
            else:
                flash('User not found.')
        elif 'add_to_cart' in request.form:
            p=request.form['buttoninput']
        #    print("hello")
        #    return render_template('index.html',shops=shops,products=products)
        else:
            return render_template('index.html',shops=shops,products=products)
        #return render_template('index.html',shops=shops,c=c,products=products)
    if request.method=="GET":
        users=db.shop_users.find()
        return render_template('index.html',shops=shops,products=products)

@app.route('/owner-home',methods=['GET','POST'])
def owner():
    global products
    products=db.products.find()
    if request.method=="POST":
        productname=request.form["productname"]
        productdescription=request.form["productdescription"]
        unitprice=request.form["unitprice"]
        quantity=request.form["quantity"]
        image=request.files['productimage']
        imagename=image.filename
        #file_path = os.path.join(app.config['STATIC_FOLDER'], imagename)
        #image.save(file_path)
        document2={
                'Product Name' : productname,
                'Product Description' : productdescription,
                'Unit Price' : unitprice,
                'Quantity' : quantity,
                #'Image' : image
            }
        db.products.insert_one(document2)
        shops=db.shop_users.find()
        allproducts=db.products.find()
        return render_template('owner-home.html',shops=shops,products=products)
    if request.method=="GET":
        return render_template('owner-home.html',products=products)

@app.route('/view_products', methods=['GET','POST'])
def view_products():
    global products
    global items
    global cart
    products=db.products.find()
    if request.method=="POST":
        j=str(request.form['productinput'])
        for i in products:
            k=str(i['_id'])
            if k==j:
                cart[k]={'Number':items,'Name':i['Product Name'],'Quantity':'1','Unit Price':i['Unit Price'],'Total':i['Unit Price']}
                print(cart)
                items+=1
        return redirect('/view_products')
    if request.method=="GET":
        return render_template('products.html',products=products)
    #return render_template('products.html',products=products)

@app.route('/checkout',methods=["GET"])
def checkout():
    if request.method=="GET":
        global cart
        global items
        print(1, cart)
        return render_template('checkout.html',cart=cart,items=items)

if __name__=="__main__":
    app.debug=True
    app.run()