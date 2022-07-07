from flask import Flask, redirect, url_for, render_template, request
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
pd.set_option('display.max_colwidth', 500)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("ExampleHome.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        URL = request.form["URL"]
        Suffix = request.form["Suffix"]
        Start = int(request.form["Start"])
        End = int(request.form["End"])
        print(URL)
        print(Suffix)
        ### Redirect to list of what you want...
        user = str(main(URL,Suffix,Start,End))
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

def main(URL,Suffix,Start,End):
    active = []
    for i in range(Start,End): #"https://people.math.carleton.ca/~awoodsid/", .html 69000, 69600 
        if i % 200==0: print("running: "+str(i))
        i = str(i)
        page = requests.get(URL+i[0:2]+"."+i[2:5]+"/"+i+Suffix)
        soup = str(bs(page.content))
        if "404" not in soup:
            active.append(i)
    
    return active

if __name__ == "__main__":
    app.run()