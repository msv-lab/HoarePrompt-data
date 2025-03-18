#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5, s1 and s2 are strings of length n consisting of '0' and '1' characters.
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
        
    #State: i = n, counter = number of differing character pairs with the special rule applied.
    return counter
    #The program returns counter which is the number of differing character pairs with the special rule applied.
#Overall this is what the function does:The function takes an integer `n` and two binary strings `s1` and `s2` of length `n` as input. It returns a count of differing character pairs between `s1` and `s2`, applying a special rule that allows skipping a pair if both characters differ and the next pair also differs and the current characters in `s1` are different from each other.

