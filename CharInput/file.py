#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

name = input("What is your name? : ")

age = input("What is your age? : ")
age = int(age)

year = datetime.date.today().year

diff = 100 - age

print(name + ", the year that you will be 100 years old is : " + str(year + diff))