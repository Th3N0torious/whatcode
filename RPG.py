#import random imports the random module, which contains a variety of things to do with random number generation
import random
#The constants in the string module can be used to specify categories of characters such as ascii_letters and digits.
import string

#Characters available for password.
#Password_Characters = list(string.ascii_letters + string.digits + string.punctuation)
alphabet = list(string.ascii_letters)
integers = list(string.digits)
special_characters = list(string.punctuation)
Password_Characters = list(string.ascii_letters + string.digits + string.punctuation)
print("Random password generator.")

def generate_random_password():
    Password_Length = int(input("Enter your desired password length: "))
    alphabets_count = int(input("Enter alphhabets count in password: "))
    integers_count = int(input("Enter integers count in password: "))
    special_characters_count = int(input("Enter special characters count in password: "))

    characters_count = alphabets_count + integers_count + special_characters_count

    #Now check the total length with characters sum count
    #Want to warn the user if the sum is greater than requested password length.
    if characters_count > Password_Length:
        print("Characters total count is greater than the requested password length")
        return

#Creating the Password
    password = []
#picking random alphhabets
    for i in range(alphabets_count):
        password.append(random.choice(alphabet))

#Picking random integers
    for i in range(integers_count):
        password.append(random.choice(integers))

#Picking random special characters_count
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

#If the total character count is less than the password Password_Length
#add radom characters to make it equal to the length requested.

    if characters_count < Password_Length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(Password_Characters))
#Now the password will be shuffled
    random.shuffle(password)

#convert the list to a string and print the result
    print("".join(password))

#Invoking the function
generate_random_password()

#Next goal is to have the script create a txt file to store the password. however the script must check
#to ensure that no existing file with the same name exists. If it does add a numerical value to end of file name.

#Create a .txt file to store Password.

def save_file():
#Open a file for writing and create it if it does not exist.
    save = open("RandomPassword.txt", "w+")
    for i in range(1):
        save.write("Here is your randomly generated password: " + join(password))
save_file()

input("Pres enter to exit the Random Password Generator: ")
