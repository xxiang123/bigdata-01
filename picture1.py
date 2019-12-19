from matplotlib import pyplot as plt
import myproject.myspark



x=range(len(myproject.myspark.list_name))
plt.bar(x,myproject.myspark.list_score,align='center')
plt.xticks(x,myproject.myspark.list_name,rotation=45)
'''
x=myproject.myspark.list_name
y=myproject.myspark.list_score
plt.bar(list(x),list(y))
'''
plt.title('The show of movie score')
plt.ylabel('score')
plt.xlabel('movie name')
plt.show()

