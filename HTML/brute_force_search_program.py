#Place N queens such that no two attack each other and N = 8
# one queen in each row and column. No QUEEN ON SAME DIAGONAL
#cells [i1, j1] and [i2,j2] are on same daigonal if [i1 - i2] = [j1 - j2]
import itertools as it
def is_solution(perm):
    for(i1,i2) in it.combinations(range(len(perm)),2):
        if abs(i1-i2) == abs(perm[i1] - perm[i2]):
            return False
    return True
for perm in it.permutations(range(8)): #iterating on all possible solutions on checking if there's a solution
    if is_solution(perm):
        print (perm)
        exit()



#Answer - (0, 4, 7, 5, 2, 6, 1, 3)
