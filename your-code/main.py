#1. Import the NUMPY package under the name np.

import numpy as np


#2. Print the NUMPY version and the configuration.

print(np.__version__)
#1.26.1
print(np.show_config())


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

        # Method 1:
a = np.random.random((2, 3, 5))
        # Method 2:
# a = np.random.rand(2, 3, 5)
        # Method 3:
# a = np.random.randn(2, 3, 5)


#4. Print a.
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5, 2, 3))


#6. Print b.

print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
if a.size == b.size:
        print("Both arrays have the same size")
else:
        print("These arrays have different sizes")

#8. Are you able to add a and b? Why or why not?

try:
        print(a + b)
except ValueError:
        print("The sum is not possible because these arrays have different shapes")
        

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose((1, 2, 0))

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
try:
        d = a + c
        print("Sum was possible because a and c have the same shapes")
except:
        print("Sum was not possible. These arrays have different shapes")


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print(d)
print("d is the same as a, but every element of the d array is one int higher. That's because every element of c was 1")


#12. Multiply a and c. Assign the result to e.

e = a * c

#13. Does e equal to a? Why or why not?

if e.all() == a.all():
        print("These arrays are the same. e array is the result of multipling the array a to an array of 1, which equals a")


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.amax(d)
d_min = np.amin(d)
d_mean = np.mean(d)
print(f"The max value of d is {d_max}, the min is {d_min}, and the mean is {d_mean}")

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty([2,3,5])


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

for i in range(2): #d[0] o d[1]
        for j in range(3): #d[0][0] o d[0][1] o d[0][2] o d[1][0] o d[1][1] o d[1][2]
                for k in range(5): #d[0][0][0] o d[0][0][1] o d[0][0][2] o d[0][0][3] o d[0][0][0][4]...
                        if d_min < d[i][j][k] < d_mean:
                                f[i][j][k] = 25
                        if d_mean < d[i][j][k] < d_max:
                                f[i][j][k] = 75
                        if d_mean == d[i][j][k]:
                                f[i][j][k] = 50
                        if  d_min == d[i][j][k]:
                                f[i][j][k] = 0
                        if  d_max == d[i][j][k]:
                                f[i][j][k] = 100
f

"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print(d)
print(d_min, d_mean, d_max)
print(f)


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
g = f.astype('object') 
for i in range(2):
        for j in range(3):
                for k in range(5):
                        if d_min < d[i][j][k] < d_mean:
                                g[i][j][k] = "B"
                        if d_mean < d[i][j][k] < d_max:
                                g[i][j][k] = ("D")
                        if d_mean == d[i][j][k]:
                                g[i][j][k] = "C"
                        if  d_min == d[i][j][k]:
                                g[i][j][k] = "A"
                        if  d_max == d[i][j][k]:
                                g[i][j][k] = "E"
print(g)