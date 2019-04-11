#there are 3 sticks with n discs sorted by size on one of the sticks. the goal is to move all n discs to another stick subject to two constraints: move one disc at a time and dont' place a larger disc on a smaller one
#it is possible foe every value n
#it is possible for n = 1,2,3
#so to solve for n, we need to know how to solve n-1, and for that we need n-2 etc..
#so this process is called induction
#PROGRAM FOR STEP BY STEP MOVES
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print "Move disk 1 from rod",from_rod,"to rod",to_rod
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print "Move disk",n,"from rod",from_rod,"to rod",to_rod
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
print (TowerOfHanoi(6,'A','B','C'))


#PROGRAM TO CALUCULATE NO.OF MOVES
# it is known that the number of moves is 2^n-1
import math
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print "Move disk 1 from rod",from_rod,"to rod",to_rod
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)

    print "Move disk",n,"from rod",from_rod,"to rod",to_rod
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
print (TowerOfHanoi(6,'A','B','c'))
totalMoves = ((math.pow(2, 6))- 1)
print (totalMoves)
