# strings
a = "23sdfr%"
print (a)
b = 'as#2134'
print (b)
c = type ('56')
print (c) #anything within single or double quotes will be a string
#string concatination
d=a+b
print (d) # 23sdfr%as#2134
e='7'
print (int(e) + 1) #int() is used to convert  string to int. So 8

#use indexing to replace the string
day = 'today is friday'
print (day[9:15]) #prints friday

#if the end digit after the colon is n't specified, then it prints till the end
print (day[5:]) #prints is friday

#Similarly, if the first digit before the colon isn't specified, then it takes from the first
print (day[:4]) #prints today

#python also supports negative indexing
print (day[-6:-1]) #prints frida
print (day[-6:]) #prints friday

# You can duplicate data by multiplication
print (a * 3) # 23sdfr%23sdfr%23sdfr%

s="Python is fun"
print(s[7:9]) # pritns is
print (s[-3:0]) # prints none
print (s[-3:-1]) # prints fu
print (s[-3:]) # prints fun
print (s[-3:][-1]) # prints n
