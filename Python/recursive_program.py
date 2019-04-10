#Alice and Bob are in line. Alice found out there are 240 people before her and Bob found out there are 249 people before him
#so here's how to find out no.of people before you
#numberOfPeopleBefore(A):
#    if there is nobody before A:
#        return 0
#    B<- person right before A
#    return numberOfPeopleBefore(B) + 1
#recursive - pgm calls itself
#factorial - for a positive integer n, the factorial n is the product of integers from 1 to n
#n! = 1 if n = 1
#n! = n (n - 1)! if n>1

#one way - summing
def factorial(n):
    assert (n>0)
    result = 1
    for i in range (1, n+1):
        result *= i
    return result
print (factorial(5))

#second way - recirsive
def factorial2(p):
    assert (p>0)
    if p == 1:
        return 1
    else:
        return (p * factorial2(p-1))
print (factorial2(5))
#one must ensure that a recursive pgm terminates ar a finite no. of steps
# this is achieved by decreasinf some parameters until it reaches a base case
# so for line problem above
# line length decrease by 1 with each recursive call until it becomes 1
# factorial: n decrease to 1


# example for infinte recursion
def infinite(h):
    if n == 1:
        return 0
    return (h * infinite( h + 1 ))

#example for infinite recursion - no base case
def fac(j):
    return (j * fac(n-1))

#parameter doesnt change
def infinite2 (k):
    if k ==1:
        return 0
    return (1 + infinite2 (k))
