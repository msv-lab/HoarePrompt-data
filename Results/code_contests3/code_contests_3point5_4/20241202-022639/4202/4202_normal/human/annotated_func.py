#State of the program right berfore the function call: a and b are 01-strings of length between 1 and 1000, containing only "0" and "1" characters.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are 01-strings of length between 1 and 1000, containing only "0" and "1" characters; `pa` is equal to the number of occurrences of '1' in the input string
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are 01-strings of length between 1 and 1000, `pa` is equal to the number of occurrences of '1' in the input string, `pb` is equal to the number of occurrences of '1' in the input string
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` calculates the number of occurrences of '1' in two input strings of 01-characters of length between 1 and 1000. It then prints 'YES' if the count of '1's in the first string is greater than or equal to the count of '1's in the second string; otherwise, it prints 'NO'. The function does not accept any parameters and returns nothing.

