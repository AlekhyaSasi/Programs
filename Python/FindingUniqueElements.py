# solution 1
#v1 = [1,2,3,2,3,5]
#v2 = list()
#for i in xrange(0, len(v1)):
#    if v1[i] in v2:
#        continue

#    v2.append(v1[i])

#print (v2)

#solution 2
v1 = [1,2,3,2,3,5]
v2 = list()
b = False
v2.append(v1[0])
for i in xrange(1, len(v1)):
    for j in xrange(0, len(v2)):
        if v1[i] == v2[j]:
            b = True
            break
        else:
            b = False
    if b == False:
        v2.append(v1[i])
print (v2)
