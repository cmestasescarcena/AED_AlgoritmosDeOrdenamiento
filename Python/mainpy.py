import pandas as pd
import numpy as np
import time

inicio = time.time()

data = pd.read_csv("D:\\TAREA01\\AED_AlgoritmosDeOrdenamiento\\Data\\100.csv", header=None)
array = data[0].to_numpy()
print(array)

#BUBBLE SORT O BURBUJA
time.sleep(1)
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

fin = time.time()
print("\nTiempo de ejecución", fin-inicio)

#MERGE SORT
def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = array[l + i]
 
    for j in range(0, n2):
        R[j] = array[m + 1 + j]
        
    i=0
    j=0
    k=1
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(array, l, r):
    if l < r:
 
        m = l+(r-l)//2
        mergeSort(array, l, m)
        mergeSort(array, m+1, r)
        merge(array, l, m, r)
 
n = len(array)
print("Given array is")
for i in range(n):
    print("%d" % array[i],end=" ")
 
mergeSort(array, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % array[i],end=" ")