#State of the program right berfore the function call: s is a string of length n (1 ≤ n ≤ 100), consisting of only "U" and "D", where "U" represents a coin facing up and "D" represents a coin facing down.
def func_1(s):
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns 'YES'
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function accepts a string `s` consisting of 'U' and 'D', where 'U' represents coins facing up and 'D' represents coins facing down. It checks if the number of 'U' (coins facing up) is odd. If the count of 'U' is odd, the function returns 'YES', indicating that the string can be read from start to end without ever having more 'D' than 'U'. Otherwise, it returns 'NO', indicating that such a condition cannot be met.

