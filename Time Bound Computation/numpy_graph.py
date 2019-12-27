import matplotlib.pyplot as plt


#x and y for NumPy python
x = [1,5,10,50, 100, 500, 1000]
y = [0.000768899917602539, 0.00258779525756835, 0.00220608711242675, 0.00296616554260253, 0.005051851272583, 0.784027099609375, 8.45831394195556]

#plotting the graph
plt.plot(x, y, 'x-',label='NumPy Python', marker='o', color='b')

# labeling the x axis
plt.xlabel('Dimension of Matrix (n x n)')
# labeling the y axis
plt.ylabel('Time (in seconds)')

# giving a title to my graph
plt.title('How Long NumPy Python Takes to Multiply Matrices')


# function to show the plot
plt.show()
