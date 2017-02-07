#Try to print out number 10 only from the following dictionary.
money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
li = list(money["under_bed"])
print ("The list of dictioanry 'money' values: ", li)
print ("Display only 10: ", li[1])
