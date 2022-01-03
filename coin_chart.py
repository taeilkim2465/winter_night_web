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

def Achange(A, nowt):
  return A

def Bchange(B, nowt):
  if random.random() > 0.95:
    B += 100
  return B + random.randrange(-2, 16)

Cphase = 'UP1'
# UP1 UP2 DOWN1 DOWN2
def Cchange(C, nowt):
  global Cphase
  if C > 2000:
    Cphase = 'DOWN1'
  elif C < 500:
    Cphase = 'UP2'
  elif Cphase == 'UP2' and C > 1500:
    Cphase = 'DOWN2'
  if Cphase == 'UP1':
    return C + random.randrange(-20, 60)
  elif Cphase == 'UP2':
    return C + random.randrange(-20, 100)
  elif Cphase == 'DOWN1':
    return C + random.randrange(-100, 20)
  else:
    return C + random.randrange(-30, 20)

def Dchange(D, nowt):
  if D == 0:
    return 0
  nomean = random.random() > 0.5
  nomean2 = random.random() > 0.4
  if nomean2:
    D += random.randrange(-30, 30)
  elif nomean:
    D*=1.2
  else:
    D/=1.2
  if D <= 0:
    return 0
  else:
    return D
  # return D

def Echange(E, nowt):
  if E==0:
    return 0
  if nowt>82:
    E += random.randrange(-30, 250)
  else:
    E += random.randrange(-30, 6)
  if E<=0:
    return 0
  else:
    return E

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

# while True:
#   if int(nowtime:=time.time()-t)%10==0:
#     fluctuation(coins_dict, nowtime)
#     time.sleep(2)
#   if nowtime>40:
#     break

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