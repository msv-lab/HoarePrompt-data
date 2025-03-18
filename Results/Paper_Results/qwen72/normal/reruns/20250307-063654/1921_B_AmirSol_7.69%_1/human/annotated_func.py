#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^5, s1 and s2 are strings of length n consisting of '0' and '1' characters, and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: `n` is a positive integer such that 1 <= n <= 10^5, `s1` and `s2` are strings of length `n` consisting of '0' and '1' characters, `counter` is the number of positions where `s1` and `s2` differ, and `i` is `n`.
    return counter
    #The program returns the number of positions where the strings `s1` and `s2` differ.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and two strings `s1` and `s2` of length `n` consisting of '0' and '1' characters. It returns the number of positions where `s1` and `s2` differ, with a special rule: if two consecutive positions differ and the characters at these positions in `s1` are also different, they are counted as a single difference. After the function concludes, `n` remains a positive integer such that 1 <= n <= 10^5, and `s1` and `s2` are unchanged.

