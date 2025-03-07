#State of the program right berfore the function call: s is a string consisting of 'U' and 'D' characters, representing the initial state of the coins where 'U' means the coin is facing up and 'D' means the coin is facing down. The length of s is a positive integer n (1 ≤ n ≤ 100).
def func_1(s):
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns 'YES'
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function accepts a string `s` consisting of 'U' and 'D' characters, representing the initial state of coins where 'U' means the coin is facing up and 'D' means the coin is facing down. It returns 'YES' if the number of 'U' characters in the string is odd, otherwise it returns 'NO'.

