#List Datatypes
#declaring a list
li= ['hi', 3, 'murthy']
print ("Index 2 value", li[2]) # list supports indexing
#Type of the list
print ("Type of li is ", type (li))
#Length of the list
print ("Length of li ", len(li))
#delete an element in the list with the index number
del li[2]
print ("After deleting 3rd element in the list", li)
#Multiply the list
print ("Multiplying the list", li*2)
#Add the element to the list
#ERROR 'LIST OBJECT IS NOT CALLABLE' -For accessing the elements of a list you need to use the square brackets ([]) and not the parenthesis (()).
li.append(444)
print ("Appending a value to the list", li)
#to add an element at a particular position
li.insert(2, 'murthy')
print ("Inserting a value to the list in the index-2",li)
#to remove an element from the list
li.remove(444)
print ("Removing a value from the list", li)

#the command 'dir(list)' in the command prompt to know more list fnctions
# the command 'help.list(function_name)' displays the method discription

#you can create list with different functions
def changeme( mylist ):
    "This changes a passed list into this function"
    extendedList = mylist.extend([1,2,3,4]) #append takes one values but you can add multiple values in []. However, the values remain the [] while displaying. Hence, use 'extend' to literally extend the list
    return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
# Function definition is here
newList = [li, mylist]
print ("New List", newList)

a=[1,2,3,4,5]
a.remove(3)
print(a[3])
