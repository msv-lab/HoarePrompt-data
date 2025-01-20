#State of the program right berfore the function call: t is a non-empty string consisting only of lowercase Latin letters, and its length does not exceed 100 characters.
def func_1(t):
    n = len(t)
    for i in range(1, n):
        if t[:i] == t[-i:]:
            s = t[:-i]
            if s + t[-i:] == t:
                return 'YES\n' + s
        
    #State of the program after the  for loop has been executed: If there exists an `i` such that `t[:i] == t[-i:]` and `s + t[-i:] == t`, the output is 'YES\n' followed by `s`. Otherwise, the output is 'NO'.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a non-empty string `t` consisting only of lowercase Latin letters, and its length does not exceed 100 characters. It checks if there exists an index `i` such that the prefix `t[:i]` is equal to the suffix `t[-i:]`. If such an `i` is found, the function returns 'YES\n' followed by the string `t` with the suffix `t[-i:]` removed. If no such `i` exists, the function returns 'NO'.

