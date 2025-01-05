#State of the program right berfore the function call: a and b are 01-strings (strings containing only the characters "0" and "1") with lengths between 1 and 1000 inclusive.
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the count of '1's in the input string, `a` is a 01-string, `b` is a 01-string.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the count of '1's in the input string, `a` is a 01-string, `b` is a 01-string, `pb` is the count of '1's in the input from `raw_input()`.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function reads two binary strings from user input, counts the number of '1's in each string, and prints 'YES' if the count of '1's in the first string is greater than or equal to that in the second string; otherwise, it prints 'NO'. It does not accept parameters and does not handle invalid input cases.

