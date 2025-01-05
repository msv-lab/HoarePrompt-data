#State of the program right berfore the function call: a and b are strings containing only "0" and "1" characters, with lengths between 1 and 1000.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings containing only "0" and "1" characters, with lengths between 1 and 1000; `pa` is equal to the total number of '1' characters in the input
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings containing only "0" and "1" characters, with lengths between 1 and 1000; `pa` is equal to the total number of '1' characters in the input, `pb` is the total number of '1' characters encountered during the execution
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` processes two input strings `a` and `b`, which consist of only "0" and "1" characters and have lengths between 1 and 1000. It calculates the total number of '1' characters in each string, stores them in variables `pa` and `pb`, and then prints 'YES' if `pa` is greater than or equal to `pb`, otherwise it prints 'NO'. The function does not explicitly return any value.

