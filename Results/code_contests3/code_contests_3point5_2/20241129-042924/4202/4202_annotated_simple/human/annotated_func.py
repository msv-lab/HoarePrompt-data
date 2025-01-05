#State of the program right berfore the function call: a and b are strings consisting of only "0" and "1" characters, and 1 ≤ |a|, |b| ≤ 1000.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the total count of '1's in the input string
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is the total count of '1's in the input string, `pb` is the total count of '1's in the input string
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function `func` takes no parameters but operates on two strings `a` and `b`, which consist only of "0" and "1" characters with lengths between 1 and 1000. It calculates the total count of '1's in both strings and prints 'YES' if the count of '1's in string `a` is greater than or equal to the count of '1's in string `b`, otherwise it prints 'NO'.

