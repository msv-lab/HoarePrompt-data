#State of the program right berfore the function call: a and b are strings consisting of only "0" and "1" characters, and the length of a and b is between 1 and 1000, inclusive.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings consisting of only "0" and "1" characters with length between 1 and 1000, inclusive; `pa` is the number of occurrences of '1' in the input string
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings consisting of only "0" and "1" characters with length between 1 and 1000, inclusive; `pa` is the number of occurrences of '1' in the input string, `pb` is equal to the number of occurrences of '1' in the input string
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:Functionality: The function calculates the number of occurrences of '1' in two input strings a and b, and then prints 'YES' if the count of '1's in a is greater than or equal to the count of '1's in b; otherwise, it prints 'NO'. The function does not actually perform a bitwise XOR operation between the strings a and b as mentioned in the annotation. It only compares the counts of '1's in the two strings and prints the result based on that. Missing functionality includes performing the XOR operation or returning the result as a new string.

