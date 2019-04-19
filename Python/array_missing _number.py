#How do you find the missing number in a given integer array of 1 to 100?
#You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in list. One of the integers is missing in the list. Write an efficient code to find the missing integer.
#In order to avoid Integer Overflow, we can pick one number from known numbers and subtract one number from given numbers.



def get_missing_no(a,n):
    #a = []
    #for j in range (1,101):   #if you need 1-100
    #    a.append(j)
    #    print (a)
    x1 = a[0]
    x2 = 1

    for i in range(1,n):  #XOR all the array elements, let the result of XOR be X1.
        x1 = x1 ^ a[i]

    for i in range(2,n+2): #XOR all numbers from 1 to n, let XOR be X2.
        x2 = x2^i

    return x1 ^ x2  #XOR of X1 and X2 gives the missing number.


a = [1, 2, 4, 5, 6]
n=len(a)
missing_number = get_missing_no(a,n)
print(missing_number)
