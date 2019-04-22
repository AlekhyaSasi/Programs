
#Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.
#Python has a built-in class called Counter forx convinent tallies
def majority(a):
    counts = {} #empty dictionary
    for i in range(len(a)):
        b = a[i] #temp value
        if b in counts:
            counts[b] = counts[b] + 1
        else:
            counts[b] = 1
    #print(counts)
    max_value = max(counts.values())
    #print (max_value)
    for i in counts.keys():
        if counts[i] == max_value:
            print ("majority element is", +i)
a = [1,2,3,1,5,2,1,1,4]
majority(a)


#A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
#Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
#Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising a KeyError
#https://docs.python.org/2/library/collections.html#collections.Counter
from collections import Counter
def majority_element(a):
    count = Counter(a)
    value, count = count.most_common()[0]
    print(value)

a = [1,2,3,1,5,2,1,1,4,7,8,9,1,4,4,4,4,4,1,3,3,3,3,3,3]
majority_element(a)

def majority_element_another(a):
    print(max(set(a), key = a.count))
