#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5, and s1 and s2 are strings of length n consisting of '0' and '1'.
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
        
    #State: Output State: The `counter` variable will be incremented for each position `i` where `s1[i]` is different from `s2[i]`, and the following conditions are met:
    #
    #- If `i < n - 1` and `s1[i + 1]` is different from `s2[i + 1]` and `s1[i]` is different from `s1[i + 1]`, then `counter` is incremented by 1 and `i` is incremented by 2.
    #- Otherwise, `counter` is incremented by 1 and `i` is incremented by 1.
    #
    #The final value of `counter` will be the total number of positions where `s1` and `s2` differ, considering the special condition for consecutive differing bits in `s1`.
    #
    #In simpler terms, the `counter` will count the number of positions where `s1` and `s2` differ, but it will also increment the counter an additional time if there are two consecutive differing bits in `s1` at those positions.
    return counter
    #The program returns the counter which counts the number of positions where `s1` and `s2` differ, and additionally increments by 1 whenever there are two consecutive differing bits in `s1` at those positions.
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 10^5) and two strings `s1` and `s2` of length `n` consisting of '0' and '1'. It returns a count of the number of positions where `s1` and `s2` differ, and increments this count by 1 for each pair of consecutive differing bits in `s1` at those positions.

