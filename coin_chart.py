import random
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import csv
import pandas as pd
import coin_fluc as coin

filepath = os.path.dirname(os.path.realpath(__file__))
dataname = 'CoinData.csv'

coins_dict = {
  'AltF4coin': 1000,
  'Bytecoin': 1000,
  'Coincoin': 1000,
  'Doggycoin': 1000,
  'Eithereum': 1000
}

Color_dict = {
  'RED': (255, 0, 0),
  'BLUE': (0, 0, 255),
  'GRAY': (155, 155, 155)
}

A_Color = 'GRAY'
B_Color = 'GRAY'
C_Color = 'GRAY'
D_Color = 'GRAY'
E_Color = 'GRAY'

x = []
y = []

figure, ax = plt.subplots(figsize=(4,3))
line, = ax.plot(x, y)
# plt.axis([0, 4*np.pi, -1, 1])

x_value = 0
total_1 = coins_dict['AltF4coin']
total_2 = coins_dict['Bytecoin']
total_3 = coins_dict['Coincoin']
total_4 = coins_dict['Doggycoin']
total_5 = coins_dict['Eithereum']

fieldnames = ["x_value","total_1","total_2","total_3","total_4","total_5"]
 
with open(os.path.join(filepath, dataname),'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()

def func_animate(i):
    global x_value, total_1, total_2, total_3, total_4, total_5, coins_dict
    if x_value<120:
      with open(os.path.join(filepath, dataname),'a') as csv_file:
          csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
  
          info = {
              "x_value":x_value,
              "total_1":total_1,
              "total_2":total_2,
              "total_3":total_3,
              "total_4":total_4,
              "total_5":total_5
          }
  
          csv_writer.writerow(info)
          print(x_value,total_1,total_2,total_3,total_4,total_5,time.time())
  
          x_value += 1
          coins_dict = coin.fluctuation(coins_dict, x_value)
          total_1 = coins_dict['AltF4coin']
          total_2 = coins_dict['Bytecoin']
          total_3 = coins_dict['Coincoin']
          total_4 = coins_dict['Doggycoin']
          total_5 = coins_dict['Eithereum']
 
    # time.sleep(0.5)
    data =pd.read_csv(os.path.join(filepath, dataname))
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    y3 = data['total_3']
    y4 = data['total_4']
    y5 = data['total_5']
 
    plt.cla()
    plt.plot(x,y1, label='AltF4coin')
    plt.plot(x,y2,label='Bytecoin')
    plt.plot(x,y3,label='Coincoin')
    plt.plot(x,y4,label='Doggycoin')
    plt.plot(x,y5,label='Eithereum')
    
    plt.legend(loc = 'upper left')
    plt.tight_layout()


ani = FuncAnimation(figure,
                    func_animate,
                    frames=1,
                    interval=50)

ani.save(r'animation.gif', fps=10)

plt.show()