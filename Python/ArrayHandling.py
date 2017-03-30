##solution 1
#num_array = list()
#num = raw_input("Enter no. of elements:")
#print ("Enter the numbers in array:")
#for i in range(int(num)):
#    n = raw_input("number :")
#    num_array.append(int(n))
#print ("ARRAY: ", num_array)
#myset = set(num_array)
#print (list(myset))


# Solution 2
#var= [2,3,4,5,2,1]
#output = set(var)
#for x in var:
#    output.add(x)

#print (list(output))

# solution 1
v1 = [1,2,3,2,3,5]
v2 = list()
v2.append(v1[0])
for i in xrange(1, len(v1)):
    if v1[i] in v2:
        continue

    v2.append(v1[i])

print (v2)

#solution 2





#used=set()
#a = [1,0,8,2,1,5,6]
#unique = [x for x in a if x not in used and (used.add(x) or True)]
#print (unique)

#a = [1,0,8,2,1,5,6]
#unique = reduce(lambda l, x: l.append(x) or l if x not in l else l, a, [])
#print (unique)


#a = [1,0,8,2,1,5,6]
#unique = reduce(lambda l, x: l if x in l else l+[x], a, [])
#print (unique)
