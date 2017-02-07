#while loop
import getpass
password = ''
while password != 'Python123':
    password = getpass.getpass("Enter your password: ") # to hide the password use getpass
    if password == 'Python123':
        print("you are logged in!")
    else:
        print("Sorry. Try again!")
