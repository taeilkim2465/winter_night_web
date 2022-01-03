import csv
import random
import time
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas.core.indexes import interval
 
x_value = 0
total_1 = 1000
total_2 = 1000
 
fieldnames = ["x_value","total_1","total_2"]
 
with open('C:/Users/82102/Desktop/PythonWorkspace/Coin_chart/data4.csv','w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()
while True:
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
