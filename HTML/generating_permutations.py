#permuatations and combination recursive logic. so that we know how many permuattions are possible
#for the queen prob in brute force search, we are trying to find the combinations



#1.
def generate_permuatations(perm,n): # if the length of current permuattion is n then print empty perm an d return. we dont extend an empty perm
    if len(perm) == n:
        print(perm)
        return

    for k in range(n): #extend to k if lenght is not zero
        if k not in perm: #  if there's an element we check if it's present in permuation.
            perm.append(k)
            generate_permuatations(perm,n)
            perm.pop() # pop will remove the added permuatiuon s
generate_permuatations(perm = [], n = 4)

#2. now if the current partial permutation cannot be extended to a solution (i.e it already contains 2 queens that attack each other), stop trying to extend it
def can_be_extended_to_solution(perm): #perm is the partial permuation
    i = len (perm) - 1 #this is the last queen(ndex) value

    for j in range(i): #then we iterate on previous indices
        if i-j == abs (perm[i] - perm[j]): #we don't use |i-j| here because we know that i>j, and i is the last value of permuatation
            return False
    return True # if true then the current permutation can be extended to a solution

#now combining one and two
def extend(perm,n): # if the length of current permuattion is n then print empty perm an d return. we dont extend an empty perm
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n): #extend to k if lenght is not zero
        if k not in perm: #  if there's an element we check if it's present in permuation.
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm,n)

            perm.pop() # pop will remove the added permuatiuon s
extend(perm = [], n = 20)
#solution - [0, 2, 4, 1, 3, 12, 14, 11, 17, 19, 16, 8, 15, 18, 7, 9, 6, 13, 5, 10]
