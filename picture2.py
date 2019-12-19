from pyspark import SparkConf
from pyspark import SparkContext
import os
from matplotlib import pyplot as plt

os.environ['JAVA_HOME']='/usr/lib/jvm/jdk1.8.0_211'
conf=SparkConf().setAppName("myapp").setMaster("local")
sc=SparkContext(conf=conf)
lines=sc.textFile("file:///home/student/PycharmProjects/untitled1/myproject/text.txt")
rdd=lines.map(lambda x:x.split(" "))
newrdd=rdd.map(lambda x:(x[2],1))
secrdd=newrdd.reduceByKey(lambda x,y:x+y)
list=[]
list=secrdd.collect()
list_type=[]
list_num=[]
sum=0
for t in list:
    list_type.append(t[0])
    sum+=t[1]
    list_num.append(t[1])
for i in range(len(list_num)):
    t=1.0*list_num[i]/sum
    list_num[i]=t


plt.pie(list_num,labels=list_type,autopct='%1.1f%%',shadow=True,startangle=10000,pctdistance=0.9)
plt.axis('equal')
plt.legend()
plt.show()

