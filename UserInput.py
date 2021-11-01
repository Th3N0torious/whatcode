#HardCoded Garbage
#Name = input("What is your name?: ")
#Age = int(input("Enter your age: ")
#Year = int(input("What year is it?: "))
#year = str((2021 - Age)+100)
#print(Name + "You will be 100 years old in the year " + year)

#imports date class from datetime module.
import datetime
#Triggers an input response for user to enter their name.
name = input("what is your name?: ")
#Triggers an input response for user to enter their age.
age = input("Enter your age: ")
#datetime.datetime.now() returns a date object assigned to the now variable.
now = datetime.datetime.now()

diff= 100 - int(age)
print('Hi' + name + "You will be 100 years old in",(now.year + diff))
