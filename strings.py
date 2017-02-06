# strings
a = "23sdfr%"
print (a)
b = 'as#2134'
print (b)
c = type ('56')
print (c) #anything within single or double quotes will be a string
#string concatination
d=a+b
print (d)
e='7'
print (int(e) + 1) #int() is used to convert  string to int
#use indexing to replace the string
day = 'today is friday'
print (day[9:15])
#if the end digit after the colon is n't specified, then it prints till the end
print (day[5:])
#Similarly, if the first digit before the colon isn't specified, then it takes from the first
print (day[:4])
#python also supports negative indexing
print (day[-6:-1])
print (day[-6:])
print (a * 3)
