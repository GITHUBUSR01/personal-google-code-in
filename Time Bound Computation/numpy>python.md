### Why NumPy with Python is Faster Than Regular Python

  As far as data goes, my data proves that NumPy with python is faster than Regular Python. Here is my data: 
(https://github.com/GITHUBUSR01/personal-google-code-in/blob/master/Time%20Bound%20Computation/regvsnumpygraph.py)

This data shows that the two are around the same while muiltiplying smaller martices, like 5x5 or 10x10 take around the same time, 
whether you are using NumPy or not. But when it came to bigger matrices, like 500x500, or even 1000x1000, the regular python really takes
off. For 500x500, regular took 103.815311908721 seconds (1.7302551984786834 minutes), while it took NumPy Python only 0.784027099609375
seconds (0.013067118326822917 mintues!). Whille multiplying two 1000x1000 matrices, it took around 910.2915461063385 seconds (15.17152576843897549 
minutes) for regular Python and only 8.45831394195556 seconds for NumPy. There are many reasons why this came into play, but here is a few:

1. Numpy is written mostly in C, which makes it extremly fast. This is because C is a low-level language, so it is really easy for the computer
to process and understand the lanugage
   1. Looping over lists in Python is slow because the lanugage is dymanically typed. Even thought Python is also written in C, it still is
   slower.
   2. Python is interpreted and C is compiled. Compiling takes less time than interpreting. 
2. NumPy lists are often of smaller size and take up less space than regular Python lists, which leads to better runtime overall. 
    1. Python lists take up: 64 + 8 * len(lst) + len(lst) * 28 bytes, while NumPy lists take up 96 + n * 8 Bytes, in which n = length of the list.
    The smaller the lists are, the faster it will take to process it. (Data from: (https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference)
    2. 
3. NumPy is also a lot more functional than regular arrays and gives us a lot of additional features. 
    1. For example, in Python, we cannot randomly create
a martix, we have to first define a function, in which a random matrix is built for you and then loop that function, to actually make it look like a matrix Meanwhile, in NumPy, we just use np.random.randint(int, size=(x dimension ,y dimension)), in which int is
up to what integer do you want in your array. This means with NumPy, the code will be much more concise. 

