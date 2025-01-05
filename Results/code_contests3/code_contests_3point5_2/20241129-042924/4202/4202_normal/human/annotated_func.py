#State of the program right berfore the function call: a and b are strings of 01-characters with lengths between 1 and 1000.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings of 01-characters with lengths between 1 and 1000, `pa` is the number of '1's in the input
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings of 01-characters with lengths between 1 and 1000, `pa` is the number of '1's in the input, `pb` is the number of '1's in the input
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` does not accept any parameters. It operates on two variables `a` and `b`, both strings of 01-characters with lengths between 1 and 1000. It calculates the number of '1's in each string and prints 'YES' if the count of '1's in `a` is greater than or equal to the count of '1's in `b`, otherwise it prints 'NO'. The function does not have a specific return value mentioned in the provided information.

