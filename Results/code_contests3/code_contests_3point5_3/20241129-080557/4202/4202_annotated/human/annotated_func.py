#State of the program right berfore the function call: a and b are strings containing only the characters "0" and "1", with lengths between 1 and 1000.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings containing only the characters "0" and "1", with lengths between 1 and 1000; `pa` is the number of occurrences of '1' in the input string
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings containing only the characters "0" and "1" with lengths between 1 and 1000, `pa` is the number of occurrences of '1' in the input string `a`, `pb` is the number of occurrences of '1' in the input string `b`
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` processes two input strings `a` and `b`, which consist of only '0's and '1's and have lengths between 1 and 1000. It calculates the number of occurrences of '1' in each string, stores them in variables `pa` and `pb`, and then prints 'YES' if `pa` is greater than or equal to `pb`, otherwise it prints 'NO'. The function does not accept any parameters explicitly, it directly interacts with the input strings `a` and `b`.

