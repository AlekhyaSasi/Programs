#dictionaries datatypes
#similar to lists. But we have the control on indexing unlike lists.
#in short dicitonary is a pair of keys and values
#curly braces for dictionary
dict = {"Name": "Sasidhar", "Profession": "SDE"}
#to access a value of the dictionary
print ("Value of Name in Dictionary", dict["Name"])
#type of Dictionary
print ("Type of Dict", type(dict))
#to extract only values of the dictionary
print ("Values in the dict are: ", dict.values())
#dict.values() is another data type.
print ("the type of dict.values is: ", type(dict.values()))
#if you need values to be returned as a list datatype
a=list(dict.values())
print ("The list a: ", a)
