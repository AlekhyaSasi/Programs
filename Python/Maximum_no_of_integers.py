#what is the max no. of 2 digit integers (10,11,12,---99) that one can select if it is not allowed to select x and y such that x +y = 100
#ex: if x is 10, y cannot be 90, similarly 11 n 89
# there are 40 pairs (10,90), (11,89), (49,51)
# 10 numbers without pairs - 50,91, ...99
# so no more than 40+ 10 = 50 (any solution cannot be nore than size of 50)
# optimal solution is : 50, 51, ---99
# the maximum no. of 2 digit numbers s.t no two numbers of them sum up to 100 is 50
# solution of size: 50, 51, ---99 (the sum of any two is greater than )

for x in range (10,99):
    i = 0
    a = []
    for y in xrange (10,99):
        if (x + y != 100):
            i = i + 2
            a.append(x)
            a.append(y)
        else:
            i = 0

print (i)
print (len(a))
