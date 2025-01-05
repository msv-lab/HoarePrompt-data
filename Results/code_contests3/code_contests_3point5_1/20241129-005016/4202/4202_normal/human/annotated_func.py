#State of the program right berfore the function call: a and b are 01-strings containing only the characters "0" and "1" with lengths between 1 and 1000 inclusive.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are 01-strings containing only the characters "0" and "1" with lengths between 1 and 1000 inclusive; `pa` is the total count of '1's in the user inputs
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are 01-strings containing only the characters "0" and "1" with lengths between 1 and 1000 inclusive; `pa` is the total count of '1's in the user inputs, `pb` is the total count of '1's in the user inputs
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` takes no parameters and operates by processing two strings `a` and `b`. Both `a` and `b` are 01-strings containing only "0" and "1" with lengths between 1 and 1000 inclusive. The function then counts the number of '1's in each string, compares the counts, and prints 'YES' if the count of '1's in `a` is greater than or equal to the count of '1's in `b`, otherwise it prints 'NO'.

