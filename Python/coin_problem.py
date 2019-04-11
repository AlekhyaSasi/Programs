#PROVE that any monetary amount starting from 8 can be paid using coins of denomination 3 and 5
#8 = 3 + 5; 9 = 3 + 3 + 3; 10 = 5 + 5; 11 = 3 + 3 + 5
# but how can we be sure that it is always possible?
# we know how to pay 8. so 11 = 8 + 3 (adding one 3 coin) then 14, 17, 20 etc...
# similarly 9 gives 12, 15, 18, 21 etc
#while 10 gives 13, 16, 19, 22, etc..

def change (amount):
    assert (amount >= 8)
    if amount == 8:
        return [3,5]
    if amount == 9:
        return [3,3,3]
    if amount == 10:
        return [5,5]
    coins = change (amount - 3)  #u keep subtracting numbers so that we arrive at 8/9/10
    coins.append(3)
    return coins

print (change(41))
