#Question 1
#This function is used to show the average of three given numbers

def average(num1, num2, num3):
    '''Take 3 numbers and recieve their average'''
    return (num1 + num2 + num3)/3
print (average(7,5,9))
print(average(6,6,7))

#Question 2
#This is a test to see if the order of having the function defined after the given command errors out or not
print (average(7,5,9))
print(average(6,6,7))
def average(num1, num2, num3):
    '''Take 3 numbers and recieve their average'''
    return (num1 + num2 + num3)/3
#This errors out due to the commands attempting to execute a function that does not yet exist.
#However this does not error out right now with Question 1 being present, as it already defines the function.

#Question 3
def average(num1, num2, num3):
    '''Take 3 numbers and recieve their average'''
    return (num1 + num2 + num3)/3
print (average(7,5,9))
print(average(6,6,7))
#print(num1)
#This does not run, as far as printing num1. I am assuming this is because num1 is not a defined variable, and
#I grayed it out in a comment so that I could run the rest of the programs

#Question 4
#This function is used to convert a dog's age into human years
def dog_age_to_human(dog_age):
    '''Convert a dogs age to human age equivalent'''
    age_conversion= 24 +((dog_age -2) *4)
    return print(dog_age, "dog years is equivalent to", age_conversion, "human years.")
dog_age_to_human(11)

#Question 5
#This function is used to calculate the value of a car

def car_value(price, years_of_ownership, car_type):
    '''Gives value of car based off price, years owned, and type of car'''
    german= price * (1-(.05 * years_of_ownership))
    japanese= price * (1-(.07 * years_of_ownership))
    italian= price * (1+(.05 * years_of_ownership))
    if car_type == "German":
        print("The value of a $" + str(price), car_type, "car will be $" + str(german), "after", years_of_ownership, "years")
    elif car_type == "Japanese":
        print("The value of a $" + str(price), car_type, "car will be $" + str(japanese), "after", years_of_ownership, "years")
    elif car_type == "Italian":
        print("The value of a $" + str(price), car_type, "car will be $" + str(italian), "after", years_of_ownership, "years")

car_value(10000, 10, "German")

#Question 6
#This is the dog age conversion, but with user inputs given
def dog_age_to_human2(dog_age):
    '''Coverts dog age to human age and returns result'''
    age_conversion= 24 +((dog_age -2) *4)
    return age_conversion

print("Dog's Age Calculator:")
dogs_name= input("What is your dog's name? ")
dogs_given_age= input("How old is " + dogs_name +"?")

print("Your", str(dogs_name), "is " + str(dog_age_to_human2(int(dogs_given_age))) + " human years old")

#Question 7
#This is used to calculate the price of an ice cream cone

def ice_cream_cone_price(scoops):
    '''Gives price of ice cream based on scoops served'''
    price= (scoops * 1.15) +2.25
    return price

print("Ice Cream Cone Price Calculator")
scoop_amount= input("How many scoops would you like?")
print("A",scoop_amount, "scoop cone will cost $" + str(ice_cream_cone_price(int(scoop_amount))))

#Extra Credit
