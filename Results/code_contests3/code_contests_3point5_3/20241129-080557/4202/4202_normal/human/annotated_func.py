#State of the program right berfore the function call: a and b are strings consisting only of "0" and "1" characters, with lengths between 1 and 1000.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the number of times the character '1' appears in the input string
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the number of times the character '1' appears in the input string, `pb` is equal to `pa`
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` does not accept any parameters. It iterates over two input strings `a` and `b`, counting the occurrences of the character '1' in each string. Then, it prints 'YES' if the count of '1's in string `a` is greater than or equal to the count in string `b`, otherwise it prints 'NO'. The function processes strings containing only "0" and "1" characters with lengths between 1 and 1000.

