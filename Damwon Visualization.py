#Damwon Visualization

#The purpose of this program is to take a look back at the 
#Spring and Summer seasons for the World Champions in League of Legends,
#Damwon Gaming. 
#Similar to 2019, Damwon started out with a middling run in Spring LCK
#Then made a run to the top
#The purpose of the project is just to provide a snapshot in both of their seasons.
#I might incorporate some machine learning just for fun.

#Import Dataset
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

spring = pd.read_csv(r'D:\Youtube\Data Analysis\Damwon Spring.csv')
summer = pd.read_csv(r'D:\Youtube\Data Analysis\Damwon Summer.csv')
#print(spring)
#print(summer) 

labels = spring['player']
spring_kda = spring['kda']
spring_app = spring['appearances']
summer_kda = summer['kda']
summer_app = summer['appearances']

#Spring Summary
x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x-width/2, spring_kda, width, label='KDA')
rects2 = ax.bar(x + width/2, spring_app, width, label='Appearances')

ax.set_ylabel('KDA')
ax.set_title('Damwon Players by Appearances and KDA - Spring 2020')
ax.set_xticks(x)
ax.set_xticklabels(labels)
#ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()

#Summer Summary
labels = summer['player']
summer_kda = summer['kda']
summer_app = summer['appearances']

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x-width/2, summer_kda, width, label='KDA')
rects2 = ax.bar(x + width/2, summer_app, width, label='Appearances')

ax.set_ylabel('KDA')
ax.set_title('Damwon Players by Appearances and KDA - Summer 2020')
ax.set_xticks(x)
ax.set_xticklabels(labels)
#ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()

