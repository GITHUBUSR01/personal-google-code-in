import matplotlib.pyplot as plt


#x and y for regular Python
a = [1,5,10,50, 100, 500, 1000]
b = [0.00022411346435546875, 0.0004210472106933594, 0.0015130043029785156, 0.24194788932800293, 1.176138162612915, 94.86313390731812, 1118.2308418750763]

plt.plot(a, b, 'b-', marker='o', color='b')

# labeling the x axis
plt.xlabel('Dimension of Matrix (n*n)')
# labeling the y axis
plt.ylabel('Time (in seconds)')

# giving a title to my graph
plt.title('The Switched Order of Looping')


# function to show the plot
plt.show()
