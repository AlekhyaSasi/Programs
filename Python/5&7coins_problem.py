#Pay Any Large Amount with 5- and 7-Coins. the amount is in the range of 24 to 1000 
def change (amount):
    assert (amount >= 24 and amount <=1000)

    if amount == 24:
        #print ("in 24")
        return [5, 5, 7, 7]

    if amount == 25:
        #print ("in 25")
        return [5,5,5,5,5]

    if amount == 26:
        #print ("in 26")
        return [7,7,7,5]

    if amount == 27:
        #print ("in 27")
        return [5,5,5,7,5]

    if amount == 28:
        #print ("in 28")
        return [7,7,7,7]

    if amount == 29:
        #print ("in 29")
        return [5,5,7,7,5]

    if amount == 30:
        #print ("in 30")
        return [5,5,5,5,5,5]

    if amount == 49:
        #print ("in 49")
        return [7, 5, 5, 5, 5, 5, 5, 5, 7]


    coins = change (amount - 5)
    coins.append(5)
    return coins

x = change(44)
print (x)
print (sum(x))
