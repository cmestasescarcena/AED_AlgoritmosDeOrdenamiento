import pandas as pd
import numpy as np
import time

inicio = time.time()

data = pd.read_csv("../Data/100.csv", header=None)
array = data[0].to_numpy()

#MERGE SORT
def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = array[l + i]
 
    for j in range(0, n2):
        R[j] = array[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1
 

def mergeSort(array, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(array, l, m)
        mergeSort(array, m+1, r)
        merge(array, l, m, r)
 
 
# Driver code to test above
n = len(array)
print("Given array is")
for i in range(n):
    print("%d" % array[i],end=" ")
 
mergeSort(array, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % array[i],end=" ")