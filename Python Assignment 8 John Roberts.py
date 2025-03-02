#Question 1
#This code compares two phrases entered by the user and compares them to see if they are the
#same, with the first phrase being in lower case and the second phrase being in all upper case.

phrase1 = ''
phrase2 = 'filler'

while phrase2 != phrase1.upper():
    phrase1 = input("Enter a phrase: ")
    phrase2 = input("Please enter the same phrase in upper case: ")
    if phrase2 == phrase1.upper():
        print("Stop shouting please!")
    else:
        print("Please try again")

#Question 2
#This code counts the number of vowels in a users input and prints the amount

user_input= input("Please enter a word to check how many vowels it contains: ")
vowels=['a','e','i','o','u','A','E','I','O','U']
total=0

for letters in user_input:
    if letters in vowels:
        total= total+1

print("The number of vowels in", user_input, "is", total)

#Question 3
#This code checks two inputs against each other to see which word comes first and second
#alphabetically

first_word= input("Please enter a word: ")

second_word= input("Please enter a second word: ")

if first_word < second_word:
	print(first_word, "comes before", second_word)
else:
	print(second_word, "comes before", first_word)

#Question 4
#This code is used to verify that the email addresses entered by a user match, and if they do
#not then they will be prompted to try again.

email= ''
email_2= '.'

while email != email_2:
    email= input("Please enter your email address: ")
    email_2= input("Please enter your email address again: ")
    if email != email_2:
	    print("Your email address entries do not match. Please try again: ")
    else:
	    print("Email address entry verified!")

#Question 5
#This code compares the time it takes to execute a factorial using recursion versus using
#iteration.

import time

'''This function is used to find the factorial of a given number using recursion.'''
def factorial(num1):
    if num1 == 0 or num1== 1:
        return 1
    else:
        return num1 * factorial(num1-1)

print(factorial(8))

'''This function is used to find the factorial of a given number using iteration.'''
def factorial_iteration(num2):
    result=1
    for factors in range(1, num2+1):
        result= result * factors
    return result

print(factorial_iteration(8))


start = time.perf_counter_ns()
factorial(200)
stop = time.perf_counter_ns()
result=float((stop - start)//1000)
rounded_result=round(result,5)
print("The time for the recursive factorial of", 200,  "was", rounded_result, "microseconds.")

start = time.perf_counter_ns()
factorial_iteration(200)
stop = time.perf_counter_ns()
result_iteration=float((stop - start)//1000)
rounded_result_it=round(result_iteration,5)
print("The time for the iterative factorial of", 200,  "was", rounded_result_it, "microseconds.")

start = time.perf_counter_ns()
factorial(50)
stop = time.perf_counter_ns()
result=float((stop - start)//1000)
rounded_result=round(result,5)
print("The time for the recursive factorial of", 50,  "was", rounded_result, "microseconds.")

start = time.perf_counter_ns()
factorial_iteration(50)
stop = time.perf_counter_ns()
result_iteration=float((stop - start)//1000)
rounded_result_it=round(result_iteration,5)
print("The time for the iterative factorial of", 50,  "was", rounded_result_it, "microseconds.")

start = time.perf_counter_ns()
factorial(4)
stop = time.perf_counter_ns()
result=float((stop - start)//1000)
rounded_result=round(result,5)
print("The time for the recursive factorial of", 4,  "was", rounded_result, "microseconds.")

start = time.perf_counter_ns()
factorial_iteration(4)
stop = time.perf_counter_ns()
result_iteration=float((stop - start)//1000)
print("The time for the iterative factorial of", 4,  "was", rounded_result_it, "microseconds.")