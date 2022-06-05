
import requests

from bs4 import BeautifulSoup
Movienumber=input("Please enter number if movies: ")

url="https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count=%E2%80%9D"+ Movienumber
req= requests.get(url)

temp=BeautifulSoup(req.content,"html.parser")

print (temp.prettify())

for x in temp.findAll("div",class_="lister-item-content"):
 print(x.h3.a.text)
print(x.find("span",class_="genre").text)
print(x.find("div",class_="inline-block ratings-imdb-rating").text)





