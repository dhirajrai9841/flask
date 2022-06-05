# -*- coding: utf-8 -*-
"""
Created on Tue May 24 18:23:04 2022

@author: raidh
"""


set={"a","b","c"}
print(set)

dict={'name':'dhiraj','age':'24'}

print (dict)
print(dict['name'])
print(dict.keys())
print(dict.values())

dict['mobile']=1234235325
print(dict)
dict.update({'address':'sydney'})
print(dict)
dict.pop('mobile')
print(dict)
dict.popitem()
print(dict)

a="100"
b="20"
c="100"
if a!=b:
    print("a is not equal to b")
elif b!=c:
    print("b is not equal to c")
else:

     print ("a is equal to c")
     
     
     
temp=[1,2,3,4,5,6]
for i in temp:
    print (i)
    if i==4 :
      print ("sucess")
    
    
    