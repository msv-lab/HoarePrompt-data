#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), s1 and s2 are strings of length n consisting of '0' and '1' characters, where '1' indicates the presence of a cat and '0' indicates the absence of a cat.
def func_1(n, s1, s2):
    counter = 0
    i = 0
    while i < n:
        if s1[i] != s2[i]:
            if i < n - 1 and s1[i + 1] != s2[i + 1] and s1[i] != s1[i + 1]:
                counter += 1
                i += 2
            else:
                counter += 1
                i += 1
        else:
            i += 1
        
    #State: `n` is a positive integer (1 ≤ n ≤ 10^5), `s1` and `s2` are strings of length `n` consisting of '0' and '1' characters. The loop has finished executing, so `i` is equal to `n`. The `counter` variable contains the total number of times a character in `s1` was different from the corresponding character in `s2`, considering the special case where consecutive different characters in `s1` and `s2` are also different from each other in `s1`.
    return counter
    #The program returns the total number of times a character in `s1` was different from the corresponding character in `s2`, considering the special case where consecutive different characters in `s1` and `s2` are also different from each other in `s1`.
#Overall this is what the function does:The function `func_1` accepts three parameters: `n` (a positive integer), `s1`, and `s2` (two strings of length `n` consisting of '0' and '1' characters). It returns the total number of positions where the characters in `s1` and `s2` differ. If two consecutive positions in `s1` and `s2` differ and the characters in `s1` at these positions are also different, the function counts this as a single difference. The final state of the program is that `n`, `s1`, and `s2` remain unchanged, and the function has returned the computed count.

