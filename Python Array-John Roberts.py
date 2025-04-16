#Question 1
# This is creating a 5x5 randomly generated array with the integers 0-24
import numpy
np= numpy
array = np.random.randint(0, 25, size=(5, 5), dtype=int)

#Question 2
# This is simply printing the entire 5x5 randomly generated array
print("Question 2 Results:")
print(array)

#Question 3
# This is printing the number from the second row, third column
print("Question 3 Results:")
print(array[1,2])

#Question 4
# This is printing the sum of all the elements in the array
print("Question 4 Results:")
print(np.sum(array))

#Question 5
# This is printing the mean of each row in the array
print("Question 5 Results:")
print(np.mean(array, axis=1))

#Question 6
# This is printing the largest value of each column in the array
print("Question 6 Results:")
print(np.max(array, axis=0))

'''
Question 2 Results:
[[24 20 12 13  3]
 [ 4 18 11  7 21]
 [10 16 17  2  3]
 [ 1  0  9 11  0]
 [ 7  2  3  8 10]]
 
Question 3 Results:
11

Question 4 Results:
232

Question 5 Results:
[14.4 12.2  9.6  4.2  6. ]

Question 6 Results:
[24 20 17 13 21]
'''