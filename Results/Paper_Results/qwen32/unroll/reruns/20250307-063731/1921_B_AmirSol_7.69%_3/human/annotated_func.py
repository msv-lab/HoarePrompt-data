#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5, s1 and s2 are strings of length n consisting of '0's and '1's.
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
        
    #State: `i` is `n`, `counter` is the number of effective differing pairs between `s1` and `s2` as per the loop's logic.
    return counter
    #The program returns the number of effective differing pairs between `s1` and `s2` as per the loop's logic.
#Overall this is what the function does:The function takes two binary strings `s1` and `s2` of equal length `n` and returns the count of positions where the characters in `s1` and `s2` differ, considering specific patterns of differences.

