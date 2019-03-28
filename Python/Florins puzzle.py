#Person A has an unlimited number of 7-florin coins, person B has an unlimited number of 13-florin coins. How A can pay 5 florins to B?
for x in range(0,11):
    for y in xrange(0, 11):
        required_output = 7*x-13*y
        if (required_output == 5):
            print ("7 florins:", x)
            print ("13 florins:", y)

#for 1000 range
#for x in range(0,1000):
#    for y in xrange(0, 1000):
#        required_output = 7*x-13*y
#        if (required_output == 5):
#               sol = True
#                break
#   if sol = True:
#        break
# print ("7 florins:", x)
# print ("13 florins:", y)
