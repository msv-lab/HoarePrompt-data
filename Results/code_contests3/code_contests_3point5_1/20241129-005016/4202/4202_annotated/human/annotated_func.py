#State of the program right berfore the function call: a and b are strings of 0s and 1s with lengths between 1 and 1000 inclusive.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings of 0s and 1s with lengths between 1 and 1000 inclusive, `pa` is the count of '1's in the input string
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings of 0s and 1s with lengths between 1 and 1000 inclusive, `pa` is the count of '1's in the input string, `pb` is equal to the count of '1's in the input string
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` calculates the number of '1's in two input strings `a` and `b`, then prints 'YES' if the count of '1's in `a` is greater than or equal to the count of '1's in `b`, otherwise it prints 'NO'. The function does not accept any parameters and does not return any value.

