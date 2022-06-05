
from xml.dom.minidom import Attr
import requests
from bs4 import BeautifulSoup


Movienumber=input("Please enter number of movies: ")
print(Movienumber)


url="https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="+Movienumber
print(url)

req= requests.get(url)
temp=BeautifulSoup(req.content,"html.parser")

temp1 = temp.findAll("h3",class_="lister-item-header")
for x in temp1:
   print (x.a.text)
   print(x.find("span",class_="genre").text)
   print(x.find("div",class_="inline-block ratings-imdb-rating").text)
   


   










        
        
        
    

    