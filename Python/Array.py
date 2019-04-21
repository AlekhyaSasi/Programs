#Given an array A of N positive integers and another number X. Determine whether or not there exist two elements in A whose sum is exactly X.
#lets understand the question
#let's say a =[1,2,3,4,5] x = 5, sum = 3 +2, so elements are s=2, b =3 which makes the answer as Yes
#let's say a = [10,15,20,30,45,60] x = 79, but there are no elements which form the sum. Hence the is no
def sum(n,x,a):
    g = False
    for i in range(n):
        for j in range(1,n):
            if i != j:
                y = a[i] + a[j]
                if x == y:
                    g = True
                    break
        if g == True:
            break

    if g == True:
        print ('yes')
    else:
        print ('no')

a = [1,2,3,4,5,6,7,8,9,10]
sum(10,8,a)
            
