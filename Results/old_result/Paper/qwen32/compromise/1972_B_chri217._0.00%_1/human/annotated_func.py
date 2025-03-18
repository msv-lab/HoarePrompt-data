#State of the program right berfore the function call: s is a string consisting of 'U' and 'D' characters, representing the facing-up and facing-down coins respectively, and the length of s (number of coins) is a positive integer n such that 1 ≤ n ≤ 100.
def func_1(s):
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns 'YES'
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of 'U' and 'D' characters, representing facing-up and facing-down coins, respectively. It returns 'YES' if the number of 'U' characters in the string is odd, and 'NO' if the number of 'U' characters is even.

