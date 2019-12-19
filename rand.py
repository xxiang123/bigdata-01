import requests
from bs4 import BeautifulSoup
import re
import random
list=[]
for i in range(100):
    a=random.randint(10020,18960)
    list.append(a)

for i in list:
   url='http://www.k5.cc/movie/'+str(i)
   req=requests.get(url)
   html=req.text
   bf=BeautifulSoup(html,'lxml')
   div3=bf.find_all('span',class_='span_block')
   bf=BeautifulSoup(str(div3),'lxml')
   a_div=bf.find_all('a')
   if a_div:
       string=str(a_div)
       partten = re.compile('.*?([\u4E00-\u9FA5]+).*?')
       match_type = re.findall(partten, string)
       if match_type[0] in ['查看','美国']:
           break
       print(match_type)