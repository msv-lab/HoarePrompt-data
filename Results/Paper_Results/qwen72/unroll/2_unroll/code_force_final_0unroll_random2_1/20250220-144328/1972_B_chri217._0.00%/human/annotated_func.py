#State of the program right berfore the function call: s is a string of length n (1 ≤ n ≤ 100) containing only the characters "U" and "D".
def func_1(s):
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns 'YES'
    else :
        return 'NO'
        #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a string `s` of length n (1 ≤ n ≤ 100) containing only the characters "U" and "D". It returns 'YES' if the number of "U" characters in the string is odd, and 'NO' if the number of "U" characters is even. The function does not modify the input string `s`.

