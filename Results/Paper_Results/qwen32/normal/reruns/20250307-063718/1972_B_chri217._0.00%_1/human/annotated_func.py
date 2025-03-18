#State of the program right berfore the function call: s is a string of length n, where n is a positive integer (1 ≤ n ≤ 100), consisting only of the characters "U" and "D".
def func_1(s):
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns 'YES'
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_1` takes a string `s` consisting of the characters "U" and "D" and returns 'YES' if the number of "U" characters in the string is odd, otherwise it returns 'NO'.

