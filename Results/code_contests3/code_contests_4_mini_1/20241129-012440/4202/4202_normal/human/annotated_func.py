#State of the program right berfore the function call: a and b are 01-strings (strings containing only the characters "0" and "1") with lengths ranging from 1 to 1000.
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the count of '1's in the input string.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the count of '1's in the input string; `pb` is also the count of '1's in the input string.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function reads two binary strings from input, counts the number of '1's in each string, and prints 'YES' if the count of '1's in the first string is greater than or equal to the count in the second string; otherwise, it prints 'NO'. It does not accept parameters; instead, it reads input directly from the user.

