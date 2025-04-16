
#Question 1
# This is creating a 5x5 randomly generated array with the integers 0-24
import numpy
np= numpy
array = np.random.randint(0, 25, size=(5, 5), dtype=int)

#Question 2
# This is simply printing the entire 5x5 randomly generated array
print(array)

#Question 3
# This is printing the number from the second row, third column
print(array[1,2])

#Question 4
# This is printing the sum of all the elements in the array
print(np.sum(array))

#Question 5
# This is printing the mean of each row in the array
print(np.mean(array, axis=1))

#Question 6
# This is printing the largest value of each column in the array
print(np.max(array, axis=0))