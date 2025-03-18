#State of the program right berfore the function call: s is a string of length n (1 ≤ n ≤ 100), consisting of only "U" and "D", where "U" represents a coin facing up and "D" represents a coin facing down.
def func_1(s):
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns 'YES'
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of "U" and "D" characters, representing coins facing up and down respectively. It checks whether it is possible to flip some of the coins so that all coins face up ("U"). If such a configuration is possible, it returns 'YES'; otherwise, it returns 'NO'.

