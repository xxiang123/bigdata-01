#http://www.k5.cc/movie/list/---3-
# http://www.k5.cc/movie/
import requests
from bs4 import BeautifulSoup
import re
import random
'''
list=[]
list_href=[]
list_name=[]
list_score=[]
list_type=[]
'''
fp=open("text.txt",'a+')
while True:
   list = []
   list_href = []
   list_name = []
   list_score = []
   list_type = []
   for i in range(100):
      a=random.randint(23678,31960)
      list.append(a)
   #fp=open("text.txt",'a+')
   for i in list:
      url='http://www.k5.cc/movie/'+str(i)
      req=requests.get(url)
      html=req.text
      bf=BeautifulSoup(html,'lxml')
      div1=bf.find_all('h1',class_='font14w')
      div2=bf.find_all('div',style='float:left; margin-right:10px;')
      div3 = bf.find_all('span', class_='span_block')
      bf = BeautifulSoup(str(div3), 'lxml')
      a_div = bf.find_all('a')
      if div1 and div2 and a_div:
          partten =re.compile('[1-9]\d*\.\d*|0\.\d*[1-9]\d*$')
          string=str(div2)
          list_num=partten.findall(string)
          if list_num and a_div:
             list_href.append(url)
             list_score.append(float(list_num[0]))
             string=str(div1)
             partten=re.compile('.*?([\u4E00-\u9FA5]+).*?')
             match_obj=re.findall(partten,string)
             list_name.append(str(match_obj[0]))
             string = str(a_div)
             match_type = re.findall(partten, string)
             if match_type[0] in ['查看', '美国','大陆','其他']:
                 break
             list_type.append((match_type[0]))
             fp.writelines(str(match_obj[0])+' '+list_num[0]+' '+match_type[0]+' '+url+'\n')
             fp.flush()

   for i in range(len(list_type)):
      print(list_name[i])
      print(list_score[i])
      print(list_type[i])
      print(list_href[i])





