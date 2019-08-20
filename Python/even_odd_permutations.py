#write a function is_even(p) that returns True for even permutations and False for odd permutations.
def is_even(sequence):
    my_count = 0
    for i, num in enumerate(sequence, start=1):
        my_count += sum(num>num2 for num2 in sequence[i:])
    return not my_count % 2


sequence =  [0,3,2,4,5,6,7,1,9,8]
print(is_even(sequence))
