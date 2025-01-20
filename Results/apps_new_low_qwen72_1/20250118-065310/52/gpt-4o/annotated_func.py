#State of the program right berfore the function call: t is a non-empty string consisting of lowercase Latin letters, and its length does not exceed 100 characters.
def func_1(t):
    n = len(t)
    for i in range(1, n):
        if t[:i] == t[-i:]:
            s = t[:-i]
            if s + t[-i:] == t:
                return 'YES\n' + s
        
    #State of the program after the  for loop has been executed: The string `t` is a non-empty string consisting of lowercase Latin letters with a length `n` between 1 and 100 inclusive. The variable `i` iterates from 1 to `n-1`. The variable `s` is defined such that if the substring `t[:i]` equals the substring `t[-i:]`, then `s` is set to `t[:-i]`. If `s + t[-i:]` equals `t`, the program returns 'YES\n' followed by the string `s`. If no such `i` is found, the loop completes without returning anything. The variables that remain constant are `t` and `n`. After the loop, `i` will be `n` if the loop completes without returning.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` takes a single parameter `t`, which is a non-empty string consisting of lowercase Latin letters with a maximum length of 100. The function checks if the string `t` can be split into two parts such that the prefix and suffix of `t` (of the same length) are identical. If such a split is found, the function returns 'YES\n' followed by the substring of `t` that excludes the matching suffix. The possible lengths of the matching suffix are 1, 2, or 3 characters. If no such split is found, the function returns 'NO'. The original string `t` remains unchanged throughout the execution of the function.

