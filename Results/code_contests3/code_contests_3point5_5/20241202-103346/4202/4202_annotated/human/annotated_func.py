#State of the program right berfore the function call: a and b are strings consisting of only the characters "0" and "1", and the length of a and b is between 1 and 1000, inclusive.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings consisting of only the characters "0" and "1" with length between 1 and 1000, inclusive, `pa` is the total count of '1's in the input provided by the user
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings consisting of only "0" and "1" characters, `pa` is the total count of '1's in the input string, `pb` is the total count of '1's in the input string
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` does not accept any parameters. It processes two strings, `a` and `b`, which consist only of "0" and "1" characters. The length of strings `a` and `b` is between 1 and 1000, inclusive. The function calculates the total count of '1's in each string (`pa` and `pb`) and then prints 'YES' if the count of '1's in `a` is greater than or equal to the count of '1's in `b`, otherwise it prints 'NO'.

