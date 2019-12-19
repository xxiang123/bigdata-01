import requests
from bs4 import BeautifulSoup
import re
url='http://www.k5.cc'
req=requests.get(url)
bf=BeautifulSoup(req.text,'lxml')
div=bf.find_all('div',id='list2')
a_div=BeautifulSoup(str(div[0]),'lxml')
a=a_div.find_all('a')
listname=[]
listhref=[]
listnum=[]
for each in a:
    listname.append(each.string)
    listhref.append(url+each.get('href'))
for i in range(len(listname)):
    print(listname[i])
    print(listhref[i])
for url in listhref:
   req=requests.get(url)
   html=req.text
   buf=BeautifulSoup(html,'lxml')
   div=buf.find_all('div',style='float:left; margin-right:10px;')
   string=str(div[0])
   partten=re.compile('[1-9]\d*\.\d*|0\.\d*[1-9]\d*$')
   list_str=partten.findall(string)
   listnum.append(float(list_str[0]))

for each in listnum:
    print(each)