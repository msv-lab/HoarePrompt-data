#State of the program right berfore the function call: n is a positive integer (1 <= n <= 10^5), s1 and s2 are strings of length n consisting of '0' and '1' characters, where '1' indicates the presence of a cat and '0' indicates the absence of a cat.
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
        
    #State: `i` is `n`, `counter` is the number of positions where `s1` and `s2` differ, with consecutive differing positions that are not the same in `s1` counted as a single difference.
    return counter
    #The program returns the number of positions where `s1` and `s2` differ, with consecutive differing positions that are not the same in `s1` counted as a single difference.
#Overall this is what the function does:The function `func_1` accepts three parameters: a positive integer `n`, and two strings `s1` and `s2` of length `n` containing '0' and '1' characters. It returns the number of positions where `s1` and `s2` differ, with consecutive differing positions that are not the same in `s1` counted as a single difference. The final state of the program is that `i` is equal to `n`, and `counter` contains the computed number of differences.

