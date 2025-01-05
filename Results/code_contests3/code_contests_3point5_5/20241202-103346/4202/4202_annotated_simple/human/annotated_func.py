#State of the program right berfore the function call: a and b are strings of 01-characters with lengths between 1 and 1000.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings of 01-characters with lengths between 1 and 1000; `pa` is the count of '1' characters in the input string.
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: Output State: `a` and `b` are strings of 01-characters with lengths between 1 and 1000, `pa` is the count of '1' characters in the input string, `pb` is the count of '1' characters in the input string.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` reads input strings `a` and `b`, which consist of 01-characters with lengths between 1 and 1000. It then counts the occurrences of '1' in each string and prints 'YES' if the count of '1' characters in `a` is greater than or equal to the count in `b`, otherwise it prints 'NO'. The function does not accept any parameters and does not explicitly return anything.

