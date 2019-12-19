from pyspark import SparkConf
from pyspark import SparkContext
import os
list=[]
list_name=[]
list_score=[]
os.environ['JAVA_HOME']='/usr/lib/jvm/jdk1.8.0_211'
conf=SparkConf().setAppName("myapp").setMaster("local")
sc=SparkContext(conf=conf)
lines=sc.textFile("file:///home/student/PycharmProjects/untitled1/myproject/text.txt")
rdd=lines.map(lambda x:x.split(" "))
newrdd=rdd.map(lambda x:(x[0],float(x[1]))).map(lambda x:(x[0],(x[1],1))).reduceByKey(lambda x,y:(x[0]+y[0],x[1]+y[1]))
secrdd=newrdd.mapValues(lambda x:(x[0]/x[1]))
threerdd=secrdd.sortBy(ascending=False,keyfunc= lambda x:x[1])
#threerdd.foreach(print)

list=threerdd.collect()
i=0;
for t in list:
    list_name.append(t[0])
    list_score.append(t[1])
    i=i+1
    if(i==10):
        break

for i in range(len(list_name)):
    print(list_name[i],list_score[i])
