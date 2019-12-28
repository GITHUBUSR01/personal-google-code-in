import matplotlib.pyplot as plt


#x and y for regular Python
x = [1,5,10,50, 100, 500, 1000]
y = [0.0000982284545898437,0.000365972518920898,0.0017409324645996, 0.0303816795349121, 0.779442071914672, 103.815311908721, 910.2915461063385]

plt.plot(x, y, 'r-', marker='o', color='r', label="Regular Loop")

a = [1,5,10,50, 100, 500, 1000]
b = [0.00022411346435546875, 0.0004210472106933594, 0.0015130043029785156, 0.24194788932800293, 1.176138162612915, 94.86313390731812, 1118.2308418750763]

plt.plot(a, b, 'b-', marker='o', color='b', label="Switched Loop")

# labeling the x axis
plt.xlabel('Dimension of Matrix (n*n)')
# labeling the y axis
plt.ylabel('Time (in seconds)')

# giving a title to my graph
plt.title('Regular vs Switched Order of Looping')

plt.legend()

plt.show()
