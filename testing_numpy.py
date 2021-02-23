import numpy as np

my_numbers = [
    [6,5],
    [1,3],
    [5,6],
    [1,4],
    [3,7],
    [5,8],
    [3,5],
    [8,4], 
    
    ]

sums = []

for row in my_numbers:
    row_sum = row[0] + row[1]
    sums.append(row_sum)
    
print(np.shape(row_sum))
