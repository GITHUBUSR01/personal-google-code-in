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

first_data = []

for x in range(1000001):
    a = random.randint(0, 10)
    first_data.append(a)


first_mat = newMatrix(1000, 1000, first_data)

for x in range(1000001):
    a = random.randint(0, 10)
    first_data.append(a)
second_mat = newMatrix(1000, 1000, first_data)



resulting_data = []
for x in range(1000001):
    resulting_data.append(0)

result_mat = newMatrix(1000, 1000, resulting_data)

for i in range(len(first_mat)):

   for j in range(len(second_mat[0])):

       for k in range(len(second_mat)):
           result_mat[i][j] += first_mat[i][k] * second_mat[k][j]

print("Multiplying lists without numpy: ")

print(result_mat)

print(f"This program took {time.time() - start_time} seconds to run")
