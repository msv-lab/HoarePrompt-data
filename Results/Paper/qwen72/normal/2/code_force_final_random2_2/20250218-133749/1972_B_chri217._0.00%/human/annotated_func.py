#State of the program right berfore the function call: s is a string of length n (1 ≤ n ≤ 100) containing only "U" and "D", representing the state of n coins on the table, where "U" indicates the coin is facing up and "D" indicates the coin is facing down.
def func_1(s):
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns 'YES'.
    else :
        return 'NO'
        #The program returns 'NO'.
#Overall this is what the function does:The function `func_1` takes a string `s` as input, where `s` represents the state of n coins on a table, with "U" indicating a coin is facing up and "D" indicating a coin is facing down. The function returns 'YES' if the number of coins facing up is odd, and 'NO' if the number of coins facing up is even.

