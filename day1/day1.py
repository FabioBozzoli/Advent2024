import numpy as np
import pandas as pd

df = pd.read_csv("input.txt", sep = " ", header = None)
left, right = df[0], df[3]
left = np.array(left.sort_values())
right = np.array(right.sort_values())

print(abs(left-right).sum())
'''
somma = 0
for i in left:
    count = (i==right).sum()
    somma += i*count
'''

somma = ((left.reshape(-1,1) == right.reshape(1,-1)).sum(axis = 1) * left).sum()

print(somma)
