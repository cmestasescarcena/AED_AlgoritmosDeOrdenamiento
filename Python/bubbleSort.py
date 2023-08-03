import pandas as pd
import numpy as np
import time

inicio = time.time()

data = pd.read_csv("../Data/100.csv", header=None)
array = data[0].to_numpy()

def bubbleSort(array):
    n = len(array)
    swapped = False
    for i in range (n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
            if not swapped:
                return
            
bubbleSort(array)            
print("Sorted array is:")
for i in range(len(array)):
    print("% d " % array[i], end="")