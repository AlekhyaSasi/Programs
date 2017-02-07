#Tuple Datatypes
#Tuples are immutable. Hence, you cannot modifythem once created
#to create a Tuple, you need normal bracklets, unlike lists which require square brackets
t = (1, 2, 3)
 #tuples are mostly used to stored buttons, GUI, etc.. which stores object that will not change/modify
 #there is no "remove" atributes for tuples
print ("type of t", type(t))
t2 = () #empty tuple
t3 = (5, ) #single value tuple. needs to be followed by a comma
print ("tuple 3", t3)
#tuples too have indexing.
print ("tuple1 index - 2 value: ", t[2])
t2 = (1, 2, 3, 4, 5, 6, 7 ) #overwriting the t2
print ("tuple 2 values from 1 to 5 indexes", t2[1:5])
#you can overwrite an empty tuple but cannot overwrite a created ttuple
#creating a new tuple through concatination
t4 = t + t2
print ("new tuple4: ", t4)
#length of the tuple
print ("length of the tuple: ", len (t4))
#multiplying the tuple
print ("Multiplying t3: ", t3*2)
#finding the element in the tuple
print ("find 3 in tuple3: ", 3 in (t3))
#iterating the tuple
for x in t3: print ("it's there!")
#negative indexing starts from the right
#multiple objects can be comma seperated defaults to tuples
x, y, z = 1, 5, 8
print ("X", x)
print ("Y", y)
print ("Z", z)


#built in tuple functions
#Compare tuples
#print ("comparing t, t3", cmp(t, t3))
#max value in the tuple
print ("Maximum value in t2", max(t2))
#min value in the tuple
print ("Minimum value in t2", min(t2))
#convert a list to tuple
li = [1,2,3]
print ("Converting a list to tuple", tuple(li))
