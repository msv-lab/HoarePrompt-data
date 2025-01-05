#State of the program right berfore the function call: a and b are strings consisting of only "0" and "1" characters, where 1 ≤ |a|, |b| ≤ 1000.**
def func():
    pa = 0
    for i in raw_input():
        pa += i == '1'
        
    #State of the program after the  for loop has been executed: pa is incremented by the number of '1' characters in the input string
    pb = 0
    for i in raw_input():
        pb += i == '1'
        
    #State of the program after the  for loop has been executed: `pa` is updated based on the total number of '1' characters in the input string, `pb` is equal to the total number of '1' characters in the input string
    print['NO', 'YES'][pa >= pb]
#Overall this is what the function does:The function calculates the number of '1' characters in two input strings and prints 'YES' if the count of '1' characters in the first string is greater than or equal to the count in the second string, otherwise it prints 'NO'. The function does not calculate the bitwise AND of binary representations as stated in the annotations.

