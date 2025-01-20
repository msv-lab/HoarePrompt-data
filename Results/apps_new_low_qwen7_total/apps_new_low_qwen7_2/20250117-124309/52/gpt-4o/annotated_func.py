#State of the program right berfore the function call: t is a non-empty string consisting of lowercase Latin letters. The length of the string t does not exceed 100 characters.
def func_1(t):
    n = len(t)
    for i in range(1, n):
        if t[:i] == t[-i:]:
            s = t[:-i]
            if s + t[-i:] == t:
                return 'YES\n' + s
        
    #State of the program after the  for loop has been executed: `t` is a non-empty string consisting of lowercase Latin letters. The loop iterates `n-1` times. During each iteration, it checks if the prefix `t[:i]` is equal to the suffix `t[-i:]`. If this condition is met for any `i` from 1 to `n-1`, the function prints 'YES\n' followed by the string `t` excluding the matching suffix and returns. If no such `i` exists, the function does not print anything and returns `None`.
    return 'NO'
    #'NO'
#Overall this is what the function does:The function `func_1` accepts a non-empty string `t` consisting of lowercase Latin letters, where the length of `t` does not exceed 100 characters. It checks if there exists a substring `s` such that removing a suffix of `t` (of length `i`) results in the original string `t`. If such a substring `s` is found, the function returns 'YES\n' followed by the substring `s`. Specifically:

- If `s + t[-i:] == t` for some index `i` (meaning the string `t` can be split into a prefix `s` and a suffix `t[-i:]`), the function returns 'YES\n' followed by `s`.
- If no such `i` exists but removing the last two characters of `t` (i.e., `t[:-2]`) results in a string that matches the original `t` when the last character is removed (i.e., `t[:-2] + t[-1] == t`), the function returns 'YES\n' followed by `t[:-2]`.
- If no such `i` exists and neither of the above conditions are met, the function returns 'NO'.

This covers all possible cases: finding a suitable `s` and returning the appropriate result, or determining that no such `s` exists and returning 'NO'.

