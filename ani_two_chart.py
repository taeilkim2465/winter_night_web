import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas.core.indexes import interval
 
 
 
def animate(i):
    data =pd.read_csv('Coin_chart/data4.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
 
    plt.cla()
    plt.plot(x,y1, label='블로그')
    plt.plot(x,y2,label='유튜브')
    
    plt.legend(loc = 'upper left')
    plt.tight_layout()
 
ani = FuncAnimation(plt.gcf(),animate, interval = 1000)
 
plt.tight_layout()
plt.show()
