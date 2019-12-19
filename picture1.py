from matplotlib import pyplot as plt
import myproject.myspark
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-microhei.ttc')


x=myproject.myspark.list_name
y=myproject.myspark.list_score

plt.figure(figsize=(9,5))
plt.title('The show of movie score',fontproperties=font)
plt.ylabel('score',fontproperties=font)
plt.xlabel('score',fontproperties=font)
plt.bar(list(x),list(y))
plt.xticks(fontsize=6,fontproperties=font)

plt.show()
