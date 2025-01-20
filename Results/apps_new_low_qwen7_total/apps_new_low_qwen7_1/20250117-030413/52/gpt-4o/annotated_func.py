#State of the program right berfore the function call: t is a non-empty string consisting of lowercase Latin letters, and the length of the string does not exceed 100 characters.
def func_1(t):
    n = len(t)
    for i in range(1, n):
        if t[:i] == t[-i:]:
            s = t[:-i]
            if s + t[-i:] == t:
                return 'YES\n' + s
        
    #State of the program after the  for loop has been executed: Output State: The string `t` remains unchanged, `n` is the length of `t`, and `i` reaches the value of `n`. The function will return 'YES\n' followed by a substring of `t` if there exists an index `i` such that `t[:i]` is equal to `t[-i:]` for all iterations up to `n-1`. If no such index is found, the function will return nothing (i.e., it will exit without returning any value).
    #
    #To summarize:
    #- **Invariant Variables**: `t`, `n`.
    #- **Final Values**: `i` equals `n`.
    #- **Loop Behavior**: The loop iterates from `1` to `n-1`. During each iteration, it checks if the prefix of `t` of length `i` is equal to the suffix of `t` of length `i`. If this condition is met, the function returns 'YES\n' followed by the substring `t[:-i]` and stops. If the condition is not met for any `i`, the function exits without returning anything.
    #
    #Therefore, the final output state is:
    #Output State: `t` is a non-empty string consisting of lowercase Latin letters, `n` is the length of `t`, and `i` is `n`. The function will return 'YES\n' followed by a substring of `t` if there exists an index `i` such that `t[:i]` is equal to `t[-i:]` for all iterations up to `n-1`. Otherwise, the function returns nothing.
    return 'NO'
    #The program returns 'NO'
#Overall this is what the function does:The function `func_1` accepts a non-empty string `t` consisting of lowercase Latin letters with a maximum length of 100 characters. It checks for the existence of a suffix within the string `t` that matches a prefix of the same length. If such a suffix is found, the function returns 'YES' followed by the substring of `t` from the start to the position just before the matched suffix. If no matching suffix is found, the function returns 'NO'. Specifically:

- If `t[:i]` is equal to `t[-i:]` for any `i` in the range `1` to `n-1`, where `n` is the length of `t`, the function returns 'YES' followed by the substring `t[:-i]`.
- If no such `i` is found, the function returns 'NO'.

The function does not modify the original string `t`. The final state of the program after the function concludes will be:
- If the function returns 'YES', the returned string is a substring of `t` from the start to the position just before the first matching suffix.
- If the function returns 'NO', the program simply returns 'NO' without any further action on `t`.

Potential edge cases include strings of varying lengths and content, ensuring that the function behaves correctly for all valid inputs.

