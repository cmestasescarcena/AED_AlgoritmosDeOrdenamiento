import pandas as pd
import numpy as np
import time

inicio = time.time()

data = pd.read_csv("D:\\TAREA01\\AED_AlgoritmosDeOrdenamiento\\Data\\100.csv", header=None)
array = data[0].to_numpy()

class node():
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 
    
    def insert(self,val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

def inorder(root, res):
    # Recursive travesal 
    if root:
        inorder(root.left,res)
        res.append(root.val)
        inorder(root.right,res)

def treesort(array):
    # Build BST
    if len(array) == 0:
        return array
    root = node(array[0])
    for i in range(1,len(array)):
        root.insert(array[i])
    # Traverse BST in order. 
    res = []
    inorder(root,res)
    return res

print(treesort(array))