from pyspark import SparkConf
from pyspark import SparkContext
import os
from matplotlib import pyplot as plt
list=[]
list_num=[]
list_score=[]
os.environ['JAVA_HOME']='/usr/lib/jvm/jdk1.8.0_211'
conf=SparkConf().setAppName("myapp").setMaster("local")
sc=SparkContext(conf=conf)
lines=sc.textFile("file:///home/student/PycharmProjects/untitled1/myproject/text.txt")
rdd=lines.map(lambda x:x.split(" "))
newrdd=rdd.map(lambda x:(x[0],float(x[1]))).map(lambda x:(x[0],(x[1],1))).reduceByKey(lambda x,y:(x[0]+y[0],x[1]+y[1]))
secrdd=newrdd.mapValues(lambda x:(x[0]/x[1]))
threerdd=secrdd.map(lambda x:(int(x[1]),1)).reduceByKey(lambda x,y:x+y)
threerdd.foreach(print)
list=threerdd.collect()
for t in list:
    if t[0]==1:
        v='1~2'
    elif t[0]==2:
        v='2~3'
    elif t[0]==3:
        v='3~4'
    elif t[0]==4:
        v='4~5'
    elif t[0]==5:
        v='5~6'
    elif t[0]==6:
        v='6~7'
    elif t[0]==7:
        v='7~8'
    elif t[0]==8:
         v='8~9'
    else :
        v='9~10'
    list_score.append(v)
    list_num.append(t[1])

plt.bar(list_score,list_num,color='y',align='center')
plt.title('the number of score')
plt.xlabel('score')
plt.ylabel('number')
plt.show()