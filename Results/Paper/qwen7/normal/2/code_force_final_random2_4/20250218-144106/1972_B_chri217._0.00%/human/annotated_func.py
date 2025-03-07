#State of the program right berfore the function call: s is a string of length n (1 ≤ n ≤ 100), consisting only of the characters "U" and "D", where "U" represents a coin facing up and "D" represents a coin facing down.
def func_1(s):
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns 'YES'
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of characters "U" and "D". It counts the occurrences of "U" and "D" in the string. If the count of "U" is odd, the function returns 'YES'. Otherwise, it returns 'NO'.

