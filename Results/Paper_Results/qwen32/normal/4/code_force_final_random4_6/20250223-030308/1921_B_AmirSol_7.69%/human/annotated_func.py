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
        
    #State: `i` is `n` and `counter` is the number of times `s1[i]` was not equal to `s2[i]` under the specified conditions.
    return counter
    #The program returns the number of times `s1[i]` was not equal to `s2[i]` under the specified conditions.
#Overall this is what the function does:The function accepts an integer `n` and two strings `s1` and `s2`, each of length `n` consisting of '0's and '1's. It returns the number of positions `i` where `s1[i]` is not equal to `s2[i]`, considering specific conditions for consecutive mismatches.

