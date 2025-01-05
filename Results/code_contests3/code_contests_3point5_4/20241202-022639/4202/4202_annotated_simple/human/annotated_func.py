#State of the program right berfore the function call: **Precondition**: The input strings a and b are 01-strings of length between 1 and 1000, containing only the characters "0" and "1".
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the number of times '1' appears in the input string
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the number of times '1' appears in the input string, `pb` is the same as `pa`
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` does not accept any parameters. It processes two input strings, a and b, which are 01-strings of length between 1 and 1000, containing only "0" and "1" characters. The function counts the occurrences of '1' in both strings and prints 'YES' if the count of '1' in string a is greater than or equal to the count in string b; otherwise, it prints 'NO'. The function does not explicitly return a value.

