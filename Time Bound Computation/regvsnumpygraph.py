import matplotlib.pyplot as plt


#x and y for regular Python
x = [1,5,10,50, 100, 500, 1000]
y = [0.0000982284545898437,0.000365972518920898,0.0017409324645996, 0.0303816795349121, 0.779442071914672, 103.815311908721, 910.2915461063385]

plt.plot(x, y, 'r-',label='Regular Python', marker='o', color='r')

#x and y for NumPy python
z = [1,5,10,50, 100, 500, 1000]
a = [0.000768899917602539, 0.00258779525756835, 0.00220608711242675, 0.00296616554260253, 0.005051851272583, 0.784027099609375, 8.45831394195556]

plt.plot(z, a, 'b-',label='NumPy Python', marker='o', color='b')

# naming the x axis
plt.xlabel('Dimension of Matrix (squared)')
# naming the y axis
plt.ylabel('Time')

# giving a title to my graph
plt.title('Multiplying Matrices With Numpy Vs Without Numpy')

plt.legend()

# function to show the plot
plt.show()
