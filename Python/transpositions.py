#Find a sequence of transpositions of letters that transform the sequence MARINE (letters are numbered 0..5) to the sequence AIRMEN.
#Transpositions are represented by pairs of integers. For example, the pair (0,1) transforms MARINE to AMRINE.
#Transpositions are performed from left to right.
#You should define the sequence by writing something like this
#(the dots should be replaced by numbers, each pair in parentheses specifies one permutation,
#and these permutations are performed sequentially, from left to right):
#(The format looks strange if you have no experience with python, but codeblocks are the easiest way to check the answer, sorry)

#easiest way to solve it
def sequence():
    unsorted_list = ['M','A','R','I','N','E']
    sorted_list = []
    #sorted_list = ['A','I','R','M','E','N']
    ordered = [1,3,2,0,5,4]
    for i in ordered:
        #print(i - debug step
        #print(unsorted_list[i]) - debug step
        sorted_list = [unsorted_list[i] for i in ordered]
        print(sorted_list)
        return ((0,1),(1,2),(2,3),(1,2),(4,5))

print(sequence())

#take sorted sequence "AIRMEN" and store in a var
input_sorted = input("Enter post sorted sequnece divided by spaces:")
sorted_seq = [str(n) for n in input_sorted.split()]

#converting string to number and storing the number and characters in a dictionary
def stringToNum(seq):
    length = len(seq)
    sorted_list = []
    for i in range(length):
        sorted_list.append(i+1)
    sorted_dictionary = dict(zip(sorted_list, seq))

#take unsorted sequence "MARINE" and store it in a var
input_unsorted = input("Enter pre sorted sequence divided by spaces:")
unsorted_seq = [str(n) for n in input_unsorted.split()]

#comparing value of two list
def unsortedStringToNum(seq,dic):
    for item in seq:
        if item in dic.values():
                print("here")
                unsorted_dictionary = dict(zip(item, dic.values()))
                print(unsorted_dictionary)

unsortedStringToNum(unsorted_seq, dictionary)
print(unsorted_dictionary)
