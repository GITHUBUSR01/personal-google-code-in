import numpy as np

##Here are some examples of numpy functions

print(np.zeros((6,4))) #This prints an array of zeroes, given the coordinates

print(np.eye(2)) #creates a 2x2 indentity array

a = np.array( [[6, 9, 3],
               [0, 1, 9],
               [8, 1, 9]] )

b = np.array([[7, 5, 8],
               [1, 3, 4],
               [5, 5, 6]])

print(a.shape) #prints the dimensions of an array

print(len(a)) #gives us the length of the array

print(a.dtype) type of data in the arra

print(np.add(a,b)) #adds the arrays
print(np.subtract(a,b)) #subtracts the arrays
print(np.multiply(a,b)) #mutilplys the arrays
print(np.divide(a,b)) #divides the arrays
print(np.exp(a)) #exponenetation
print(np.sqrt(b)) #square root
print(np.log(a))


print(a>1) #element wise comaprision, aka checks if every number is greater than 1
print(np.array_equal(a,b)) #array wise comparison


print(a.sum()) #calculates the sum of all of the elements in an array
print(b.min()) #the smallest value in an array
print(a.max()) #the largest value in an arrya
print(b.cumsum()) #cumulative sum of elements in array
print(a.mean()) #prints the mean of all the elements in the array
print(b.std()) #prints the standard deviation of all the elements in an array

print(np.transpose(a)) #switches the rows and columns, and prints it
print(np.arange(6).reshape(3,2)) #.arrange() makes an array which goes up to the number passed, in this case 5
# .reshape() reshapes the array into a 3x2 matrix'
print(a.ravel()) #flattens an array. A is a 2d array, ravel() makes it 1d.
print(a.ravel(order="C")) #You can also set an order to the ravel() function
print(a.resize(3, 4)) #returns a new array with a 3x4 dimension shape

np.append(a, 3) #adds items to an array
np.insert(a, 3, 2)#inserts items to an array
np.delete(a, [0])
print(a)

print(np.vstack((a,b))) #vertically stacks an array, based on the rows
print(np.column_stack((a,b))) #horizontally stacks an array, based on the columns

print(np.hsplit(a,[2])) #split the array horizontally at the 2nd index
print(np.vsplit(b,[1])) #split the array vertically the 1st index
