#Loops
#fundamental building blocks for every programming language, which allows you to execute the statements multiple times
#for loop can apply on any datatype
emails = ['abc@gmail.com', 'xyz@gmail.com', 'pqr@hotmail.com']
print ("the list of email ids:")
for email in emails: #syntax is 'for var_name in iteration'
    print (email)
# printing only gmail ids
#indentation for "for" and "if loop" are imp
print ("the ids with gmail are:")
for item in emails:
    if 'gmail' in item:
        print (item)

for i in (1,2,3):
    print(i+1)

a="Tricky"
for i in a[:3]:
    print(i) #though the list has only one item, it prints based on the index i.e 3 in order of list

a=["Trickier"]
for i in a:
    print(i) #here the list has one item and the loop runs for one complete list. so it prints completely

lst=["Terribly Tricky"]
for word in lst:
    for letter in word[-6:]:
        print(letter)
#The first loop here iterates through list 'lst', pulls out the string "Terribly Tricky" and stores it in variable 'word'. Then, the nested loop iterates through the last 6 items of string "Terribly Tricky" and prints them out in each iteration.

#For Loop with Multiple lists
names = ['alekhya', 'amulya','sweta']
email_domains =['gmail', 'yahoo', 'hotmail']
for i, j in zip(names, email_domains):
    print (i, j)
    
