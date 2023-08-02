import csv
import time

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

if __name__ == "__main__":
    intentos = 15
    A = datos("..//Data//4000.csv")

    # BUBBLE SORT
    print("Bubble Sort 15 times")
    print("Result: [", end=" ")
    for i in range(intentos):
        start_time = obtenerTiempo()
        burbuja(A.copy())
        end_time = obtenerTiempo()
        elapsed_time = (end_time - start_time) / 1_000_000
        print(elapsed_time, end=" ")
    print("]")
    print()

    # TREE SORT
    print("Tree Sort 15 times")
    print("Result: [", end=" ")
    for i in range(intentos):
        start_time = obtenerTiempo()
        treeSort(A.copy())
        end_time = obtenerTiempo()
        elapsed_time = (end_time - start_time) / 1_000_000
        print(elapsed_time, end=" ")
    print("]")
    print()

    # MERGE SORT
    print("Merge Sort 15 times")
    print("Result: [", end=" ")
    for i in range(intentos):
        start_time = obtenerTiempo()
        mergeSort(A.copy())
        end_time = obtenerTiempo()
        elapsed_time = (end_time - start_time) / 1_000_000
        print(elapsed_time, end=" ")
    print("]")
    print()