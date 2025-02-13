#Question 1
#This little while loop is used to countdown from a users given input to "blastoff!!"
x= input("Please enter an integer: ")

while int(x) >0:
    print(x)
    x = int(x) - 1

print("blastoff!!")

#Question 2
#Same loop, but slightly modified to indicate if the countdown numbers are odd or even

x= input("Please enter an integer: ")

while int(x) >0:
    if int(x) % 2 ==0:
        print(x, "is even")
        x = int(x) - 1
    else:
        print(x, "is odd")
        x = int(x) - 1


print("blastoff!!")

#Question 3
#Loop with the modification of having the user determine how much the given integer is decremented

x= input("Please enter an integer: ")
y= input("Please enter an amount to decrease by: ")
while int(x) >0:
    if int(x) % 2 ==0:
        print(x, "is even")
        x = int(x) - int(y)
    else:
        print(x, "is odd")
        x = int(x) - int(y)


print("blastoff!!")

#Question 4
#This is a code for a user to enter words and have it tell them the length, unless the word is
#less than five words, in which case it terminates with "goodbye".
#I ran into an interesting issue with this; I could only get it to run correctly if I had the
#'guess' value assigned to something with a greater length than five, prior to user input.

guess= "word that is greater than five"

while len(guess) >= len("fiver"):
    guess= input("Please enter a word: ")
    if len(guess) >= len("fiver"):
        print(guess, "has", len(guess), "letters")
    else:
        print("goodbye")

#Question 4.2
#Same code, but it gives a limited number of inputs to the user

guess= "word that is greater than five"
guess_input= 0
guess_limit= 5

while len(guess) >= len("fiver") and guess_input != guess_limit:
    guess= input("Please enter a word: ")
    if len(guess) >= len("fiver"):
        print(guess, "has", len(guess), "letters")
        guess_input= int(guess_input) + 1
    else:
        print("goodbye")

print("loser")

#Question 5
#This while loop counts from 10 to 100 in decimal, binary, and hex
i=10

while i < 100:
    print(i, (bin(int(i))), (hex(int(i))))
    i +=1

#Question 6
#This while loop prints out a number of stars in descending order based on user input

def star_fall_iteration(star_entry):
    while int(star_entry) > 0:
        stars = int(star_entry) * "*"
        print(stars)
        star_entry= int(star_entry) - 1

star_fall_iteration(7)

#This recursion accomplishes the same task as the while loop

def star_fall_recursion(star_input):
    if int(star_input) > 0:
        star_amount = int(star_input) * "*"
        print(star_amount)
        star_input = int(star_input) - 1
        star_fall_recursion(star_input)
    else:
        print("")

star_fall_recursion(8)