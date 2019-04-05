#There are some books on the table. If you group them by 3, you get some number of full groups and 2 books remain; if you group them by 4, you get some number of full groups and 3 books remain; if you group them by 5, you get some number of full groups and 4 books remain. What is the number of books on the table, if it is less than 100?
#x - total no.of books
#y - total no.of 3 group books
#z - total no.of 4 group books
#p - total no.of 5 group books
#equations derived from prob
# x-2 = 3y
# x- 3 = 4z
#x-4 = 5p
for x in range(0,101):
    for y in xrange(0, 31):
        for z in xrange(0,24):
            for p in xrange (0, 19):
                if ((x - 2) == (3 * y) and (x - 3) == (4*z) and (x-4) == (5*p)):
                    print ("x", x)
                    print ("y", y)
                    print ("z", z)
                    print ("p", p)


#answer
#('x', 59)
#('y', 19)
#('z', 14)
#('p', 11)
