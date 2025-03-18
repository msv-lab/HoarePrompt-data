#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), s1 and s2 are strings of length n consisting of characters '0' and '1'.
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
        
    #State: `counter` is the number of positions where `s1` and `s2` differ, and `i` is `n`.
    return counter
    #The program returns the number of positions where `s1` and `s2` differ.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and two strings `s1` and `s2` of length `n` containing only '0' and '1'. It returns the number of positions where the characters in `s1` and `s2` differ, with a special case where if two consecutive differing characters in `s1` and `s2` are also different from each other, they are counted as a single difference. After the function concludes, `counter` holds the total count of such differences, and `i` is equal to `n`.

