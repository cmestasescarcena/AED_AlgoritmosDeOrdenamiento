import csv
import time
import math

def obtenerTiempo():
    return int(time.time() * 1_000_000)

def datos(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        return [int(row[0]) for row in reader]

def burbuja(A):
    n = len(A)
    for i in range(n):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

def treeSort(A):
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

        def insert(self, val):
            if self.val:
                if val < self.val:
                    if self.left is None:
                        self.left = TreeNode(val)
                    else:
                        self.left.insert(val)
                elif val > self.val:
                    if self.right is None:
                        self.right = TreeNode(val)
                    else:
                        self.right.insert(val)
            else:
                self.val = val

        def in_order_traversal(self):
            result = []
            if self.left:
                result += self.left.in_order_traversal()
            result.append(self.val)
            if self.right:
                result += self.right.in_order_traversal()
            return result

    root = TreeNode(A[0])
    for i in range(1, len(A)):
        root.insert(A[i])
    return root.in_order_traversal()

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

data = ["..//Data//100.csv", "..//Data//1000.csv", "..//Data//2000.csv", "..//Data//3000.csv", "..//Data//4000.csv", "..//Data//5000.csv", "..//Data//6000.csv", "..//Data//7000.csv", "..//Data//8000.csv", "..//Data//9000.csv", "..//Data//10000.csv", "..//Data//20000.csv", "..//Data//30000.csv", "..//Data//40000.csv", "..//Data//50000.csv"]
# Listas para almacenar los tiempos de ejecución de cada algoritmo
bubble_times = []
tree_times = []
merge_times = []

# BUBBLE SORT
print("Bubble Sort 15 times")
print("Result:")
for i in range(15):
    if __name__ == "__main__":
        intentos = 15
        A = datos(data[i])
        print("[")
        for i in range(intentos):
            start_time = obtenerTiempo()
            burbuja(A.copy())
            end_time = obtenerTiempo()
            elapsed_time = (end_time - start_time) / 1_000_000
            print(elapsed_time, end=", ")
            bubble_times.append(elapsed_time)  # Agregar el tiempo a la lista
        print("]")
        print()

# TREE SORT
print("Tree Sort 15 times")
print("Result:")
for i in range(15):
    if __name__ == "__main__":
        intentos = 15
        A = datos(data[i])
        print("[")
        print("Tree Sort 15 times")
        print("Result: [", end=" ")
        for i in range(intentos):
            start_time = obtenerTiempo()
            treeSort(A.copy())
            end_time = obtenerTiempo()
            elapsed_time = (end_time - start_time) / 1_000_000
            print(elapsed_time, end=" ")
            tree_times.append(elapsed_time)  # Agregar el tiempo a la lista
        print("]")
        print()

# MERGE SORT
print("Tree Sort 15 times")
print("Result:")
for i in range(15):
    if __name__ == "__main__":
        intentos = 15
        A = datos(data[i])
        print("[")
        print("Merge Sort 15 times")
        print("Result: [", end=" ")
        for i in range(intentos):
            start_time = obtenerTiempo()
            mergeSort(A.copy())
            end_time = obtenerTiempo()
            elapsed_time = (end_time - start_time) / 1_000_000
            print(elapsed_time, end=" ")
            merge_times.append(elapsed_time)  # Agregar el tiempo a la lista
        print("]")
        print()

# Calcular el promedio y la desviación estándar para cada algoritmo
def average(xs):
    return sum(xs) / len(xs)

def stand_desv(nums):
    mean = average(nums)
    sd = math.sqrt(sum((x - mean) ** 2 for x in nums) / len(nums))
    return sd

print("BubbleSort average:", average(bubble_times))
print("BubbleSort desv_stan", stand_desv(bubble_times))
print()

print("TreeSort average:", average(tree_times))
print("TreeSort desv_stan:", stand_desv(tree_times))
print()

print("MergeSort average:", average(merge_times))
print("MergeSort desv_stan:", stand_desv(merge_times))
print()