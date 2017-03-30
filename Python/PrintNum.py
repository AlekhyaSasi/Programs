#solution 1
#data = input("Enter a number: ")
#for i in range (1, data+1):
    #if i % 3 == 0:
    #    print("Fizz")
    #elif i % 5 == 0:
    #    print("Buzz")
    #else:
    #    print (i)

#solution 2
data = input("Enter a number: ")
for i in range(1, data+1):
    print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i)
