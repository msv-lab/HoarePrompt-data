#State of the program right berfore the function call: a and b are strings consisting of only "0" and "1" characters, and 1 ≤ |a|, |b| ≤ 1000.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the number of '1' characters in the input string obtained from `raw_input()`, `a` and `b` remain the same as in the initial state
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the number of '1' characters in the input string obtained from `raw_input()`, `a` and `b` remain the same as in the initial state, `pb` is the total number of occurrences of '1' in the input string after all iterations of the loop have executed.
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` does not accept any parameters. It calculates the number of occurrences of '1' characters in two input strings obtained from `raw_input()`, stored in variables `pa` and `pb`. Then, it prints 'YES' if the count of '1' characters in the first string is greater than or equal to the count in the second string, otherwise it prints 'NO'. The function works with input strings `a` and `b`, where each string consists only of "0" and "1" characters, and each string has a length between 1 and 1000 characters. The function does not explicitly return any value.

