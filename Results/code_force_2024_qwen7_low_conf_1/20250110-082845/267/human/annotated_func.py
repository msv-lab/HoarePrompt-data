#State of the program right berfore the function call: s is a string consisting of lowercase Latin letters and/or question marks, and its length is at most 5000.
def func_1(s):
    n = len(s)
    max_length = 0
    for d in range(1, n // 2 + 1):
        count = sum(1 for i in range(d) if func_2(s[i], s[i + d]))
        
        for l in range(n - 2 * d):
            if l > 0:
                count -= func_2(s[l - 1], s[l - 1 + d])
                count += func_2(s[l + d - 1], s[l + 2 * d - 1])
            if count == d:
                max_length = max(max_length, 2 * d)
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of lowercase Latin letters and/or question marks, `n` is the length of `s`, `max_length` is the maximum value found during the loop, `d` is a non-negative integer such that `2 * d <= n` and `n - 2 * d > 0`, and `l` is the last value of `l` after all iterations.
    return max_length
    #The program returns max_length, which is the maximum value found during the loop
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of lowercase Latin letters and/or question marks, and its length is at most 5000. It iterates over possible lengths of substrings `d` and checks for valid pairs within these substrings using the helper function `func_2`. For each valid pair, it updates the count of matching pairs. It then adjusts the count based on the sliding window approach. If the count equals `d`, it updates `max_length` to the maximum value found during the loop. Finally, the function returns `max_length`, which represents the maximum length of valid substrings found during the process. Potential edge cases include when the input string `s` is empty or contains only question marks, in which case `max_length` would be 0. Additionally, the function does not handle cases where `s` might contain characters other than lowercase Latin letters and question marks, though this is not explicitly stated in the problem description.

#State of the program right berfore the function call: a and b are characters, where both can be lowercase Latin letters or '?'
def func_2(a, b):
    return a == b or a == '?' or b == '?'
    #The program returns True if 'a' equals 'b', or if 'a' is '?', or if 'b' is '?'
#Overall this is what the function does:The function `func_2` accepts two parameters `a` and `b`, both of which can be lowercase Latin letters or the character `'?'`. It returns `True` if either `a` equals `b`, or if `a` is `'?'`, or if `b` is `'?'`. If none of these conditions are met, it returns `False`. This covers all possible cases for the inputs `a` and `b`.

