#State of the program right berfore the function call: a and b are strings consisting solely of the characters '0' and '1', with lengths between 1 and 1000 inclusive.
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is '0', `b` is '1', `pa` is the count of '1's in the input string.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` is '0', `b` is '1', `pa` is the count of '1's in the input string, `pb` is the total count of '1's in the input string.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function counts the number of '1's in two user-provided strings of '0's and '1's, and prints 'YES' if the first string has at least as many '1's as the second string; otherwise, it prints 'NO'. It does not accept parameters and lacks input validation for the string contents and lengths.

