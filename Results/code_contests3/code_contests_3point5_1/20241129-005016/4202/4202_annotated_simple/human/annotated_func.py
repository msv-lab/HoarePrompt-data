#State of the program right berfore the function call: a and b are strings consisting of only "0" and "1" characters, with lengths between 1 and 1000, inclusive.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings consisting of only "0" and "1" characters, with lengths between 1 and 1000, inclusive; `pa` is the total number of '1' characters in the input string
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `a` and `b` are strings consisting of only "0" and "1" characters, with lengths between 1 and 1000, inclusive; `pa` is the total number of '1' characters in the input string, `pb` is equal to the total number of '1' characters in the input string
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` reads input strings and counts the occurrences of '1' characters in each string. It then prints 'YES' if the count of '1's in the first string is greater than or equal to the count in the second string; otherwise, it prints 'NO'. The function does not have any parameters and does not return anything.

