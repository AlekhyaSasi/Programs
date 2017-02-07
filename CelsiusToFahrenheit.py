# create a function that converts Celsius degrees to Fahrenheit
#print out a message in case a number lower than -273.15 is passed as input when calling the function.
celsius = float(input('Enter a value in celsius: '))
if celsius <= -273.15:
    print ("Please enter a value above -273.15 C")
else:
    farenheit = (celsius*9/5 ) + 32
    print ("The temperature in Fahrenheit is: ", farenheit)
    def cToF(celsius):
        farenheit = (celsius*9/5 ) + 32
        return farenheit
    print ("the temperature using functions: ", farenheit)

#solution in terms of function
def c_to_f(c):
    f=c*9/5+32
    return f
print(c_to_f(10))
