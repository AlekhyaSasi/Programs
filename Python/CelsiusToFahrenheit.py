# create a function that converts Celsius degrees to Fahrenheit - 1
#print out a message in case a number lower than -273.15 is passed as input when calling the function. - 2
#temperatures=[10,-20,-289,100]Then, iterate over the temperature converter function that you created in execise 3 and print out the following output. -3
#50.0, -4.0, That temperature doesn't make sense!, 212.0 - 3


celsius = float(input('Enter a value in celsius: '))
if celsius <= -273.15:
    print ("Please enter a value above -273.15 C")
else:
    farenheit = (celsius*9/5 ) + 32
    print ("The temperature in Fahrenheit is: ", farenheit)


#iteration problem
temperatures = [10, 20, -289, 100]
def c_to_f(i):
    f=i*9/5+32
    return f

for i in temperatures:
    print (i)
    if i <= -273.15:
        print ("the temperature doesn't make sense!")
    else:
        print ("the temperature in farenheit: ", c_to_f(i))
