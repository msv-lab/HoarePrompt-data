#State of the program right berfore the function call: n is a positive integer (1 <= n <= 10^5), s1 and s2 are strings of length n consisting of '0' and '1' characters, and the sum of n over all test cases does not exceed 10^5.
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
        
    #State: `n` is a positive integer (1 <= n <= 10^5), `s1` and `s2` are strings of length `n` consisting of '0' and '1' characters, and the sum of `n` over all test cases does not exceed 10^5. The loop has completed its execution, so `i` is equal to `n`. The `counter` variable holds the number of positions in the strings `s1` and `s2` where the characters differ, and for each such position, if the next position (if it exists) also differs and the characters in `s1` at these two positions are different, then the `counter` is incremented by 1 for both positions, otherwise, the `counter` is incremented by 1 for each differing position.
    return counter
    #The program returns the value of `counter`, which is the number of positions in the strings `s1` and `s2` where the characters differ, with an additional increment for each pair of consecutive differing positions where the characters in `s1` at these two positions are different.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and two strings `s1` and `s2` of length `n` consisting of '0' and '1' characters. It returns an integer `counter` which represents the number of positions where the characters in `s1` and `s2` differ. For each pair of consecutive differing positions where the characters in `s1` at these two positions are different, the `counter` is incremented by 1 for both positions, otherwise, it is incremented by 1 for each differing position. After the function concludes, `n`, `s1`, and `s2` remain unchanged, and `counter` holds the final result.

