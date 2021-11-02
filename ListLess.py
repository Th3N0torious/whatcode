#list = [1, 23, 15, 65, 97, 30, 67, 10]
#for numbers in list:
#    if numbers >1:
#        print(list)

print("Welcome to the List Less Than Ten program..")
#\n \n creates a new line in the output of print.
print("\nEnter number as a list\n")
#The split() method splits a string into a list. The i in int(i) is a representation of user input.
a=[int(i) for i in input().split()]
#B list is using j for representation of user input then limiting input choice to only print selection if less than 5.
b=[int(j) for j in a if j<5]
print(b)
