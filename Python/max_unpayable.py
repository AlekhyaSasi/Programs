#Imagine we have only 5- and 7-coins. One can prove that any large enough integer amount can be paid using only such coins. Yet clearly we cannot pay any of numbers 1, 2, 3, 4, 6, 8, 9 with our coins. What is the maximum amount that cannot be paid?
#The maximum unpayable amount is 23. That higher numbers are payable comes from the following representations:
#24=5+5+7+7
#25=5+5+5+5+5
#26=7+7+7+5
#27=5+5+5+5+7
#28=7+7+7+7
#with the rest formed by adding 5s to these. That 23 cannot be formed can be seen by repeatedly subtracting 7 from it – 16, 9, 2, −5 – and noting that no nonnegative multiple of 5 appears.
#This is sometimes known as Sylvester's coin problem.
#The largest unpayable amount from coins of value a and b, when they are coprime, is ab−a−b.
#The takeaway from this, I think, would be that it is always good to try small examples as part of the problem solving process, so as to get a feel of what the problem's conditions and boundaries are.
#This is an instance of the Frobenius coin problem. Given two positive integers x, y with gcd(x,y)=1 the largest amount that cannot be paid with x- and y-coins is given by
N=xy−x−y .
