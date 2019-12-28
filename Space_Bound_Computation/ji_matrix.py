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

for x in range(101):
    a = random.randint(0, 10)
    first_data.append(a)


first_mat = newMatrix(10, 10, first_data)

for x in range(101):
    a = random.randint(0, 10)
    first_data.append(a)
second_mat = newMatrix(10, 10, first_data)



result_data = []
for x in range(101):
    result_data.append(0)

result_mat = newMatrix(10, 10, result_data)

for j in range(len(first_mat)):

   for i in range(len(second_mat[0])):

       for k in range(len(second_mat)):

           result_mat[j][i] += second_mat[j][k] * first_mat[k][i]

print("Multiplying lists without numpy: ")

print(result_mat)

print(f"This program took {time.time() - start_time} seconds to run")
