#State of the program right berfore the function call: s is a string of length n (1 ≤ n ≤ 100) containing only "U" and "D", representing the state of the coins.
def func_1(s):
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns 'YES'.
    else :
        return 'NO'
        #The program returns 'NO'.
#Overall this is what the function does:The function `func_1` takes a string `s` as input, where `s` is a sequence of characters "U" and "D" representing the states of coins. It counts the number of "U" characters in the string. If the count of "U" is odd, the function returns 'YES'. If the count of "U" is even, the function returns 'NO'. The function does not modify the input string `s`.

