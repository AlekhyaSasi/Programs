#python can handle both binary and text files
#read - r and write -w
#read lines
f=open("PythonInterviewQuestions.txt","r")
lines = f.readlines()
str=f.read(5)
print ("The read string is " +str)
#check current position
position = f.tell()
print ("Current file position : ", +position)
f.close()
print lines
