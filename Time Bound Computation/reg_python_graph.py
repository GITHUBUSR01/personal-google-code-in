import matplotlib.pyplot as plt


#x and y for regular Python
x = [1,5,10,50, 100, 500, 1000]
y = [0.0000982284545898437,0.000365972518920898,0.0017409324645996, 0.0303816795349121, 0.779442071914672, 103.815311908721, 910.2915461063385]

plt.plot(x, y, 'r-', marker='o', color='r')

# labeling the x axis
plt.xlabel('Dimension of Matrix (n*n)')
# labeling the y axis
plt.ylabel('Time (in seconds)')

# giving a title to my graph
plt.title('How Long Regular Python Takes to Multiply Matrices')


# function to show the plot
plt.show()
