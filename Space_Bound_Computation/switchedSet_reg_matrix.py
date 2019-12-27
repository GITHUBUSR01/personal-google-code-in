#Without numpy
import time
import random


start_time = time.time()
def newMatrix(row, col, data):
    matrix = []
    for x in range(row):
        rowList = []
        for y in range(col):
            rowList.append(data[row * x + y])

        matrix.append(rowList)
    return matrix

first_data = [0, 8, 2, 5, 8, 1, 6, 2, 5, 4, 3, 3, 4, 6, 1, 5, 0, 0, 8, 3, 1, 6, 3, 3, 1, 9, 5, 3, 3, 0, 3, 8, 0, 8, 8, 4, 6, 6, 4, 5, 3, 8, 1, 8, 7, 5, 1, 0, 5, 5, 9, 9, 6, 1, 9, 2, 6, 6, 9, 0, 3, 3, 7, 3, 8, 8, 0, 2, 2, 2, 7, 3, 1, 0, 1, 7, 5, 4, 5, 2, 7, 7, 0, 3, 5, 7, 1, 1, 5, 9, 6, 6, 5, 6, 4, 9, 6, 6, 9, 4]
# i commented this out so we can tell what the difference is
"""
for x in range(100000001):
    a = random.randint(0, 10)
    first_data.append(a)
"""

first_mat = newMatrix(10, 10, first_data)

second_data = [2, 0, 5, 8, 5, 7, 2, 9, 8, 1, 2, 1, 2, 9, 6, 0, 3, 0, 8, 4, 7, 5, 0, 0, 0, 3, 5, 0, 6, 5, 9, 3, 3, 5, 8, 8, 4, 7, 3, 1, 6, 7, 6, 9, 1, 0, 1, 9, 1, 8, 4, 6, 9, 0, 5, 0, 3, 3, 0, 6, 3, 8, 4, 5, 9, 6, 3, 5, 1, 1, 1, 2, 6, 6, 8, 9, 0, 2, 0, 6, 6, 6, 4, 9, 5, 4, 3, 6, 1, 7, 7, 9, 7, 3, 4, 3, 7, 6, 2, 0]
"""
for x in range(100000001):
    a = random.randint(0, 10)
    second_data.append(a)
"""
second_mat = newMatrix(10, 10, second_data)



result_data = []
for x in range(101):
    result_data.append(0)

result_mat = newMatrix(10, 10, result_data)

for j in range(len(first_mat)):

   for i in range(len(second_mat[0])):

       for k in range(len(second_mat)):
           result_mat[j][i] += second_mat[j][k] * first_mat[k][i]

print("Multiplying lists without numpy: ")

for x in result_mat:
    print(x)

print(f"This program took {time.time() - start_time} seconds to run")
