#Math functions in python
import math
a=15
be=22
i=9
c  = a + be
d = a - be
e = a * be
f = a / be
g = a % be
h = a ** be
print ("add -", c);
print ("Subtract -", d);
print ("multiply -", e);
print ("divide -", f);
print ("modulus -", g);
print ("power -", h);
j = math.sqrt(i)
print ("Square root - ", j)
#to know more math  functions, give 'dir<math>' in the cmd
#for order of operators look below example
k = a*be+i
l = i+a*be
m = c + a * be / i
print ("examples of order of operators")
print ("k", k)
print ("l", l)
print ("m", m)
n = c + a * be / i**2
print ("n", n) #exponent excutes first
