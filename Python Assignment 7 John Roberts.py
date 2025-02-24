#Question 1
#This code is using a for loop that prints out all of the even numbers between two given
# numbers. I had to look up how to print values in a line together using the "end" function,
#which is a helpful tool to have.

num1= input("Enter the lower number: ")
num2= input("Enter the higher number: ")
even_statement= False

for test in range(int(num1),int(num2)+1):
        if int(test) %2 ==0:
            if not even_statement:
                print("The even numbers between", num1, "and", num2, "are:", end= " ")
                even_statement = True
            print(test, end= " ")
import random
from operator import index
from turtledemo.sorting_animate import randomize

#Question 2
#This uses a while loop function to tell the user the factors of a given number. I also had
#to look up how you can append in a function, which made this vastly easier than my earlier
#attempts.

'''This function is used for giving the factors of a given number from the user.'''
def factors(number):
    iteration= 1
    factors=[]

    while int(iteration) <= int(num3):
        if int(num3) % int(iteration)==0:
         factors.append(iteration)
        iteration+=1
    return factors

num3= input("Enter a positive integer")
results= factors(num3)
print("The integers that are factors of",num3, "are: ", results)

#Question 3
#This loop gives your name a numerical value by the summation of the letters in your name
#using a list of the alphabet. Learning how index works with lists was key for this, especially
#in the placement of variables in the actual for loop.

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

user_input=input("Please enter your name: ")
total= 0

for length in user_input.lower():
    if length in alphabet:
        total += alphabet.index(length)

print(total)

#Question 4
#This code is used to take the number given by a user and print out the squares of all integers
#up to the given integer. This code was far simpler than I initially started with, as I
#initially used for loops with incrementation. But the incrementation was nullifying the base
#case, so it would loop to termination. Found some helpful tips on how small recursion loops can
#really be.

'''This function is used for printing out the square of all integers up to the given
integer from the users input.'''

def square_recursion(sqr_num):
    if sqr_num == 0:
        return
    else:
        square_recursion(sqr_num -1)
        print(sqr_num**2)

square_recursion(4)

#Question 5
#This code is used for taking an unsorted list and arranging them in a teepee formation.
#I had to look up how to put for loops with ranges into variables for this
#code, which was key to being able to complete this. Otherwise I just had two sets of for
#loops that separated my evens and odds, but I had no way to concatenate them together.

unsorted_list=[12,43,22,34,2,21,3,33,81]

even_set= [evens for evens in unsorted_list if evens %2 ==0]
odd_set= [odds for odds in unsorted_list if odds %2 !=0]

even_set.sort(reverse=True)
odd_set.sort()

print(odd_set + even_set)

#Question 6
#Hello Professor, I attempted to start on this code and below is about as far as I got before
#I was at a loss on what to do. I looked up some info on how to do this, but I did not
#recognize over half of what it was telling me to do, and I didn't want to just copy and paste
#the code without even understanding it. Is there any other tutorials that I should be
#watching for learning Python? I've been watching the 4-hour one that is assigned, but I
#have never seen most of what the solutions for this displayed.

list_number=[1,2,3,4,5,6,7,8,9,0]
result=''
result2=''

'''This function is supposed to take the given list and give the next biggest iteration of 
the given numbers. My idea was to create a recursion loop and have it loop through a 
randomization of the list until the given result was larger than the original value. But
that would simply give any number that was bigger, not the next in the iteration. Also,
for some reason it is not using the original value of 1234567890, but I could not figure
out why.'''

def next_biggest_iteration():
    global result
    global result2
    for added in list_number:
        result+= str(added)
        random.shuffle(list_number)
        for added_2 in list_number:
            result2+= str(added_2)
            if int(result2) > int(result) +1:
                return print(result2)
            else:
                next_biggest_iteration()

next_biggest_iteration()







