from flask import Flask, redirect, url_for, render_template, request
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
pd.set_option('display.max_colwidth', 500)

app = Flask("__name__", static_folder="./static")
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("ExampleHome.html")


#Flask data retrieval from login form
@app.route("/login", methods=["POST", "GET"])
def login():
    print(request.method)
    if request.method == "POST":
        print("X")
        URL = request.form["Prefix"]
        Suffix = request.form["Suffix"]
        Start = int(request.form["Start"])
        End = int(request.form["End"])
        print(URL)
        print(Suffix)
        ### Redirect to list of what you want...
        user = str(main(URL,Suffix,Start,End))
        print("XXX")
        return render_template("answer.html", Content=user)
    else:
        return render_template("index.html")

# Sends to answer page
@app.route("/<usr>")
def user(usr):
    return f"<b>{usr}</b>"


# Web Scraper Function
def main(URL,Suffix,Start,End):
    active = []
    for i in range(Start,End): #"https://people.math.carleton.ca/~awoodsid/", .html 69000, 69600 
        if i % 200==0: print("running: "+str(i))
        i = str(i)
        page = requests.get(URL+i[0:2]+"."+i[2:5]+"/"+i+Suffix)
        soup = str(bs(page.content))
        if "404" not in soup:
            textToAppend=""+URL+i[0:2]+"."+i[2:]+"/"+i+Suffix
            

            active.append(textToAppend)
    return list(active)

if __name__ == "__main__":
    app.run()