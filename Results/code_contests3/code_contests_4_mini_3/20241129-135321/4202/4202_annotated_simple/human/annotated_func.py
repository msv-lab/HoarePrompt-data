#State of the program right berfore the function call: a and b are strings consisting only of the characters '0' and '1', with lengths between 1 and 1000 inclusive.
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is a string of '0's and '1's, `b` is a string of '0's and '1's, `pa` is the count of '1's in the string returned by `raw_input()`.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is a string of '0's and '1's, `b` is a string of '0's and '1's, `pa` is the count of '1's in the string returned by `raw_input()`, `pb` is equal to `pa`, representing the total number of '1's in the input string.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function reads two binary strings from input, counts the number of '1's in each string, and prints 'YES' if the count of '1's in the first string is greater than or equal to that in the second string; otherwise, it prints 'NO'. It does not handle invalid input or input length constraints correctly.

