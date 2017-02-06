# create a function that converts Celsius degrees to Fahrenheit
celsius = int(input('Enter a value in celsius: '))
farenheit = (celsius*9/5 ) + 32
print ("The temperature in Fahrenheit is: ", farenheit)

#solution in terms of function
def c_to_f(c):
    f=c*9/5+32
    return f
print(c_to_f(10))

def cToF(celsius):
    farenheit = (celsius*9/5 ) + 32
    return farenheit
print ("the temperature using functions: ", farenheit)
