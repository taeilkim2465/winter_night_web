import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import csv
import pandas as pd

t = time.time()
print(t)
nowtime = time.time() - t

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

Aphase = 'UP1'
# UP1 UP2 DOWN1 DOWN2
def Achange(A, nowt):
  global Aphase, A_Color
  A_dif = 0
  if A > 2000:
    Aphase = 'DOWN1'
  elif A < 500:
    Aphase = 'UP2'
  elif Aphase == 'UP2' and A > 1500:
    Aphase = 'DOWN2'
  if Aphase == 'UP1':
    A_dif = random.randrange(-20, 71)
  elif Aphase == 'UP2':
    A_dif = random.randrange(-20, 101)
  elif Aphase == 'DOWN1':
    A_dif = random.randrange(-100, 21)
  else:
    A_dif = random.randrange(-30, 21)
  if A_dif > 0:
    A_Color = 'RED'
  elif A_dif < 0:
    A_Color = 'BLUE'
  else:
    A_Color = 'GRAY'
  return A + A_dif

def Bchange(B, nowt):
  global B_Color
  B_dif = 0
  if random.random() > 0.95:
    B_dif = 100
  B_dif += random.randrange(-2, 16)
  if B_dif > 0:
    B_Color = 'RED'
  elif B_dif < 0:
    B_Color = 'BLUE'
  else:
    B_Color = 'GRAY'
  return B + B_dif

Cscheduler = random.randrange(3, 8)
def Cchange(C, nowt):
  global Cscheduler, C_Color
  C_dif = 0
  if Aphase == 'DOWN1':
    if Cscheduler == 0:
      C_dif = random.randrange(-20, 101)
    else:
      Cscheduler -= 1
      C_dif = random.randrange(-15, 6)
  else:
    C_dif = random.randrange(-15, 6)
  if C_dif > 0:
    C_Color = 'RED'
  elif C_dif < 0:
    C_Color = 'BLUE'
  else:
    C_Color = 'GRAY'
  return C + C_dif

def Dchange(D, nowt):
  global D_Color
  D_dif = 0
  new_D = 0
  if D == 0:
    D_Color = 'GRAY'
    return 0
  dice = random.random()
  if dice > 0.4:
    D_dif = random.randrange(-30, 31)
    if D_dif > 0:
      D_Color = 'RED'
    elif D_dif < 0:
      D_Color = 'BLUE'
    else:
      D_Color = 'GRAY'
    if D + D_dif <= 0:
      return 0
    else:
      new_D = D + D_dif
  elif dice > 0.2:
    D_Color = 'RED'
    new_D = D*1.2
  else:
    D_Color = 'BLUE'
    new_D = D/1.2
  if new_D > 4000 or new_D < 500:
    D_Color = 'GRAY'
    return D
  else:
    return new_D

def Echange(E, nowt):
  global E_Color
  if E==0:
    E_Color = 'GRAY'
    return 0
  if nowt>80:
    E_dif = random.randrange(-30, 221)
  else:
    E_dif = random.randrange(-30, 6)
  if E_dif > 0:
    E_Color = 'RED'
  elif E_dif < 0:
    E_Color = 'BLUE'
  else:
    E_Color = 'GRAY'
  if E + E_dif <= 0:
    return 0
  else:
    return E + E_dif

def fluctuation(coindict, nowt):
  A = coindict['AltF4coin']
  B = coindict['Bytecoin']
  C = coindict['Coincoin']
  D = coindict['Doggycoin']
  E = coindict['Eithereum']

  A = Achange(A, nowt)
  B = Bchange(B, nowt)
  C = Cchange(C, nowt)
  D = Dchange(D, nowt)
  E = Echange(E, nowt)

  # print(A, B, C, D, E, nowt)
  new_dict = {
    'AltF4coin': A,
    'Bytecoin': B,
    'Coincoin': C,
    'Doggycoin': D,
    'Eithereum': E
  }
  return new_dict

x = []
y = []

figure, ax = plt.subplots(figsize=(4,3))
line, = ax.plot(x, y)
plt.axis([0, 4*np.pi, -1, 1])

x_value = 0
total_1 = coins_dict['AltF4coin']
total_2 = coins_dict['Bytecoin']
total_3 = coins_dict['Coincoin']
total_4 = coins_dict['Doggycoin']
total_5 = coins_dict['Eithereum']

fieldnames = ["x_value","total_1","total_2","total_3","total_4","total_5"]
 
with open('C:/Users/82102/Desktop/PythonWorkspace/Coin_chart/data4.csv','w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()

def func_animate(i):
    global x_value, total_1, total_2, total_3, total_4, total_5, coins_dict
    if x_value<120:
      with open('C:/Users/82102/Desktop/PythonWorkspace/Coin_chart/data4.csv','a') as csv_file:
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
          coins_dict = fluctuation(coins_dict, x_value)
          total_1 = coins_dict['AltF4coin']
          total_2 = coins_dict['Bytecoin']
          total_3 = coins_dict['Coincoin']
          total_4 = coins_dict['Doggycoin']
          total_5 = coins_dict['Eithereum']
 
    # time.sleep(0.5)
    data =pd.read_csv('Coin_chart/data4.csv')
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