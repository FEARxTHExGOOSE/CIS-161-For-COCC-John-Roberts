#Python Assignment 3

#Question 1
#This is a simple code for allowing users to enter their name after a greeting.

name= input("What is your name?")

print('Hello' + name)

#Question 2
#This is a simple input code for entering a users age, plus five years.
age= input("What is your age?")
#print("You are " + age + 5)
#This errors out due to "age" not being read as an integer
print("Your age plus five years is", int(age) + 5)

#Question 3
#This code allows a user to add a number of years to their age
year_difference= input("How many years would you like to add to your age?")
print("You will be", int(age) + int(year_difference), "in",year_difference, "years.")

#Question 4
#This code can print hours worked in decimal value
hours_worked= input("Enter the number of hours worked:")
users_worked_hours= float(hours_worked)
print("You worked", users_worked_hours, "hours this week")

pay_rate= input("Enter your hourly wage without the $:")
users_pay_rate= float(pay_rate)

#Question 5
#This code shows the total paycheck from the users entered hours and pay rate
pay_for_week= round(users_pay_rate * users_worked_hours, 2)
annual_pay= round(pay_for_week * 50, 2)
print("Your gross pay this week is $" + str(pay_for_week))
print("Your estimated annual gross pay will be $" + str(annual_pay))

#Extra Credit Code and Table Variables
#These variables are storing the values of tax percentage used based on income
gross_annual_pay= round((users_pay_rate * 40) *50, 2)
annual_pay_for_taxes= round((users_pay_rate * 40) *50, 2)
ten_percent= annual_pay_for_taxes <=11600
twelve_percent= 11600 < annual_pay_for_taxes <=47150
twenty_two_percent=47150 < annual_pay_for_taxes <=100525
twenty_four_percent=100525 < annual_pay_for_taxes <=191950
thirty_two_percent=191950 < annual_pay_for_taxes <=243725
thirty_five_percent=243725 < annual_pay_for_taxes <=609350
thirty_seven_percent=annual_pay_for_taxes >609350

print("Your gross annual pay based on a 40 hour work week with 50 weeks worked is $" + str(gross_annual_pay))

#These if and elif statements are taking the given annual pay based on the users entered pay rate
#and basing that on a 40 hour work week with 50 weeks worked, and taxing the income based on
#the tax brackets given
if ten_percent:
   print("Your annual taxed income is $", round(annual_pay_for_taxes * .90,2))
elif twelve_percent:
   print("Your annual taxed income is $", round(annual_pay_for_taxes * .88,2))
elif twenty_two_percent:
   print("Your annual taxed income is $", round(annual_pay_for_taxes * .78,2))
elif twenty_four_percent:
   print("Your annual taxed income is $", round(annual_pay_for_taxes * .76,2))
elif thirty_two_percent:
   print("Your annual taxed income is $", round(annual_pay_for_taxes * .68,2))
elif thirty_five_percent:
   print("Your annual taxed income is $", round(annual_pay_for_taxes * .65,2))
elif thirty_seven_percent:
   print("Your annual taxed income is $", round(annual_pay_for_taxes * .63,2))

