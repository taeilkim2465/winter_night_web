import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import csv
import pandas as pd

x = []
y = []

figure, ax = plt.subplots(figsize=(4,3))
line, = ax.plot(x, y)
plt.axis([0, 4*np.pi, -1, 1])

# def func_animate(i):
#     x = np.linspace(0, 4*np.pi, 1000)
#     y = np.sin(2 * (x - 0.1 * i))
    
#     line.set_data(x, y)
    
#     return line,
x_value = 0
total_1 = 1000
total_2 = 1000

fieldnames = ["x_value","total_1","total_2"]
 
with open('C:/Users/82102/Desktop/PythonWorkspace/Coin_chart/data4.csv','w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()

def func_animate(i):
    global x_value, total_1, total_2
    with open('C:/Users/82102/Desktop/PythonWorkspace/Coin_chart/data4.csv','a') as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
 
        info = {
            "x_value":x_value,
            "total_1":total_1,
            "total_2":total_2
        }
 
        csv_writer.writerow(info)
        print(x_value,total_1,total_2)
 
        x_value += 1
        total_1 = total_1+random.randint(-4,8)
        total_2 = total_2+random.randint(-5,8)
 
    time.sleep(1)
    data =pd.read_csv('Coin_chart/data4.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
 
    plt.cla()
    plt.plot(x,y1, label='A')
    plt.plot(x,y2,label='B')
    
    plt.legend(loc = 'upper left')
    plt.tight_layout()


ani = FuncAnimation(figure,
                    func_animate,
                    frames=10,
                    interval=50)

ani.save(r'animation.gif', fps=10)

plt.show()