
#Normal code
def isPlaindrome(string):
    stringCaseCheck = string.casefold() # Making the string suitable for caseless comparison
    if(stringCaseCheck==stringCaseCheck[::-1]): #Reverse the string using string slicing and compare it back to the original string.
         return "True" # If they both are equal, the strings are palindromes. Hence return 'True'
    else:
          return "False" # If they aren’t equal, the strings aren’t palindromes. Hence return 'False'

string=raw_input("Enter a string to check for Palindrome functionality:") #taking a string value from the user
isPlaindrome(string)


# code with docstring convention - pep 0257
def is_palindrome(input_string: str) -> bool:       # PEP 484
    """
    Check whether input string is a palindrome.
    Note: This does a case-insensitive check.

    :param input_string: Input string usually. ASCII encoded.
    :return: True if the input string. If not, False.
    """
    if input_string is None or len(input_string) == 0:      # None and empty string check.
        return False

    input_string = input_string.lower()                     # Lower case for case insensitivity.
    if input_string == input_string[::-1]:
        return True

    return False
