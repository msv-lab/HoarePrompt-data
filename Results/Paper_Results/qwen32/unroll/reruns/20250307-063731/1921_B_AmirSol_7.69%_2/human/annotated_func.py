#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5, s1 and s2 are strings of length n consisting only of the characters '0' and '1'.
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
        
    #State: - `i` will be equal to `n` after the loop completes because the loop increments `i` until it is no longer less than `n`.
    #- `counter` will be the total number of mismatches counted according to the rules specified in the loop.
    #
    #Output State:
    return counter
    #The program returns `counter`, which is the total number of mismatches counted according to the rules specified in the loop.
#Overall this is what the function does:The function accepts an integer `n` and two strings `s1` and `s2`, each of length `n` consisting only of the characters '0' and '1'. It returns the total number of positions at which the characters in `s1` and `s2` differ, considering specific rules for consecutive mismatches.

