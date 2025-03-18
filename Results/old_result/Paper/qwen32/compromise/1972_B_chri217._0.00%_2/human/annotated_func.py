#State of the program right berfore the function call: s is a string consisting of the characters "U" and "D" representing the states of n coins, where n is a positive integer such that 1 <= n <= 100. The function is called once per test case, and there are multiple test cases, each with its own value of n and corresponding string s.
def func_1(s):
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns 'YES'
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of characters "U" and "D". It returns 'YES' if the number of 'U' characters in the string is odd, otherwise it returns 'NO'.

