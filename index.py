from flask import Flask,render_template,request,json
from flask_pymongo import PyMongo
import requests

app=Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/kullanicilar"
mongo=PyMongo(app)


@app.route("/",methods=["GET","POST"])
def login():
	if request.method=="POST":
		mymail=request.form["mail"]
		mysifre=request.form["sifre"]
		sonuc=mongo.db.kullanici_list.find({"mail":mymail,"sifre":mysifre})
		if sonuc.count()>0:
			return render_template("index.html",kisilerim=sonuc)
		else:
			return "Boyle bir kullanıcı yoktur"

	return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
	if request.method=="POST":
		mymail=request.form["mail"]
		mysifre=request.form["sifre"]
		mongo.db.kullanici_list.insert_one({"id":1,"mail":mymail,"sifre":mysifre})
		return "kayıt tamam"
	else:
		return render_template("register.html")

@app.route("/index")
def index():
	data=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=890e1a69a5ee4904800db348aaec97be")
	dataj=data.json()
	return render_template("index.html",mydata=dataj)


app.run(debug=True)




