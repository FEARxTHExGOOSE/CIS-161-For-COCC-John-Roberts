import psutil
import requests

#Question 1
#This line of code is used to determine if a number input by a user is divisible by five.
is_divisible_by_five= int(input("Enter a number to see if it is divisible by five: "))

if is_divisible_by_five % 5 == 0:
    print(str(is_divisible_by_five) + " is divisible by five")
else:
    print(str(is_divisible_by_five) + " is not divisible by five")

#Question 2
#This code uses the if elif method for having users get the capital of a given state
state_input= input("Please enter a state to find its capital: ")

if state_input == "Oregon":
    print("Salem")
elif state_input == "Texas":
    print("Austin")
elif state_input == "Kansas":
    print("Topeka")
elif state_input == "California":
    print("Sacramento")
elif state_input == "Washington":
    print("Olympia")
elif state_input == "New Mexico":
    print("Sante Fe")

#Queston 2.1
#This code lets users get the capital of a given state using the dictionary method

state= {
    "Colorado": "Denver",
    "Nevada" : "Carson City",
    "New Jersey": "Trenton",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Rhode Island": "Providence"
}

user_input_for_state= input("Please enter a state to find it's capital: ")
capital= (state.get(user_input_for_state, "Capital was not found."))

print(capital)

#Question 2.2 Match Case Code
#This code lets users get the capital of a given state using the match case function

given_state= input("Please give a state to find it's capital: ")
match given_state:
    case "Maine":
        print("Augusta")
    case "Maryland":
        print("Annapolis")
    case "Michigan":
        print("Lansing")
    case "Minnesota":
        print("Saint Paul")
    case "Missouri":
        print("Jefferson City")
    case "Montana":
        print("Helena")

#Question 3
#This code is used for finding the price of admission based on age
'''This function is used for finding the price of admission based on age'''

def pool_admission(age):
    if int(age) < 2:
        return print(0)
    elif 2 <= int(age) <=11:
        return print(3)
    elif 11 <= int(age) <= 60:
        return print(6)
    elif int(age) > 60:
        return print(4)

pool_admission(5)

#Question 4
#This code is used to count the number of zero's in a given html

url= "http://coccbobcat.com"

response= requests.get(url)

html_content= response.text

occurences= html_content.count("160")
print(f"The substring '160' appears {occurences} times in the HTML source of http://coccbobcat.com")

#Question 5
#This code is used to determine how many processes are running on your system

running_processes = psutil.pids()
number_of_running_processes= len(running_processes)

print("The number of running processes is", number_of_running_processes)