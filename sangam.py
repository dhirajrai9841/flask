
import mysql.connector

import requests
from bs4 import BeautifulSoup


def sur(section_name,classname,url="https://www.imdb.com/title/tt0111161/?ref_=adv_li_tt"):
    req= requests.get(url)
    temp=BeautifulSoup(req.content,"html.parser")
    temp.prettify();
    temp1 = temp.find(section_name,class_=classname)
    return temp1

list=[];
# list.append(sur("span","sc-b73cd867-0 eKrKux"))
# list.append(sur("span","sc-8c396aa2-2 itZqyK"))

heading=sur("span","sc-b73cd867-0 eKrKux")
release=sur("span","sc-8c396aa2-2 itZqyK")
length=sur("ul","ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt")#sur("li","ipc-inline-list__item")
genre=sur("a","sc-16ede01-3 bYNgQ ipc-chip ipc-chip--on-baseAlt")
desc=sur("span","sc-16ede01-0 fMPjMP")
rating=sur("span","sc-7ab21ed2-1 jGRxWM")
imga="|asdas";
# sur("img","ipc-image")
video="asdsa" #=sur("video","jw-video jw-reset")
print(release)
# print(list(genre).descendants)
for x in list(genre.descendants):
    print(x)
# for x in temp1:
#    print (x.a.text)
#    print(x.find("span",class_="genre").text)
#    print(x.find("div",class_="inline-block ratings-imdb-rating").text)
   


   










        
        
        
    

    