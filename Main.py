from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random

for i in range(69000,70000):
  
    i = str(i)
    if i % 200==0: print("running: "+i)
    page = requests.get("https://people.math.carleton.ca/~awoodsid/"+i[0:2]+"."+i[2:5]+"/"+i+".html")
    soup = str(bs(page.content))
    if "404" not in soup:
        
        print(soup[280:320])
        print(i)

print("done")
