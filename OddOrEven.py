#User inputs an integer between 1 and 100.
Number_Choice = int(input("Pick a number between 1 and 100: "))
#What I want is to have it reference the value in Number_Choice.
print('You have chosen number: ' + str(Number_Choice))
#Divides number by 2 to check for odd or even
mod = Number_Choice % 2
if mod > 0:
    print ("You picked an odd number.")
else:
    print ("You picked an even number")
