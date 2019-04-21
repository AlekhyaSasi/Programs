#Given a binary number, write a program that prints 1 if given binary number is a multiple of 3.  Else prints 0. The given number can be big upto 2^100. It is recommended to finish the task using one traversal of input binary string.
#first convert binary to decimal
def binary_to_decimal(binary):
    result, i = 0,0
    while (binary!= 0):
        modulo_rem = binary % 10 #Take modulo of given binary number with 10.
        result = result + modulo_rem * pow(2,i) #Multiply remainder with 2 raised to the power and Add result with previously generated result
        binary = binary//10 #Update binary number by dividing it by 10. '//' operator to do integer division in python 3 (i.e. quotient without remainder);
        i += 1 #incrementing loop
    return result

def another_binary_to_decimal(binary):
    return int(binary,2) 

def multiple_of_3(num):
    result = binary_to_decimal(num)
    if result != 0 and result % 3 == 0:
        print ('1')
    else:
        print ('0')
multiple_of_3(11111111)
