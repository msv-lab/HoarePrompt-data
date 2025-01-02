#State of the program right berfore the function call: s is a string consisting of characters "Y", "N", and "?" representing Stepan's memory of watching episodes, where "Y" means he definitely watched the episode, "N" means he definitely did not watch it, and "?" means he is unsure.
def func_1(s):
    r = 0
    max_r = 0
    for i in range(len(s)):
        if s[i] == 'N':
            r += 1
        else:
            r = 0
        
        if r > max_r:
            max_r = r
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of characters "Y", "N", and "?"; `r` is 0; `max_r` is the maximum number of consecutive 'N' characters found in `s`.
    return max_r
    #The program returns the maximum number of consecutive 'N' characters found in the string `s`
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of characters "Y", "N", and "?". It returns the maximum number of consecutive 'N' characters found in `s`. After the function concludes, `s` remains unchanged, and the returned value is the length of the longest contiguous sequence of 'N' characters in `s`. Edge cases include an empty string, where the function returns 0, and a string with no 'N' characters, where the function also returns 0.

#State of the program right berfore the function call: s is a string consisting of 'Y', 'N', and '?' characters, and k is a non-negative integer such that 0 ≤ k ≤ len(s).
def func_2(s, k):
    s1 = 'Y' + s + 'Y'
    seq_N = s1.replace('?', 'N')
    for i in range(len(seq_N)):
        if seq_N[i:i + k] == 'N' * k:
            if s1[i - 1] in ['Y', '?'] and s1[i + k] in ['Y', '?']:
                return 1
        
    #State of the program after the  for loop has been executed: `s` is a string consisting of 'Y', 'N', and '?' characters, `k` is a non-negative integer such that 0 ≤ k ≤ len(s), `s1` is 'Y' + s + 'Y', `seq_N` is 'Y' + s.replace('?', 'N') + 'Y', and the function returns 1 if there exists an `i` such that `seq_N[i:i + k] == 'N' * k` and both `s1[i - 1]` and `s1[i + k]` are in `['Y', '?']`. If no such `i` is found, the function returns `None`.
    return 0
    #The program returns 0
#Overall this is what the function does:The function `func_2` accepts a string `s` consisting of 'Y', 'N', and '?' characters, and a non-negative integer `k` such that 0 ≤ k ≤ len(s). It modifies the string by adding 'Y' at both the beginning and end, replaces all '?' characters with 'N', and then checks if there exists a substring of length `k` that consists entirely of 'N' characters, surrounded by either 'Y' or '?'. If such a substring is found, the function returns 1. Otherwise, it returns 0. The function does not modify the original string `s` or the integer `k`.

