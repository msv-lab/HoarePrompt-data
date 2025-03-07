#State of the program right berfore the function call: s is a string of length m comprising only the first k lowercase English alphabets, k and n are positive integers such that 1 <= n <= 26 and 1 <= k <= 26.
def func_1(s, k, n):
    s1 = ''
    s2 = ''
    alphabet = {chr(i) for i in range(97, 97 + k)}
    for i in s:
        if i in alphabet:
            if len(alphabet) != 1:
                alphabet.remove(i)
            else:
                s2 += i
                alphabet = {chr(i) for i in range(97, 97 + k)}
            s1 += i
        
    #State: Output State: `s1` is a string containing all characters from `s` that are in the first `k` lowercase English alphabets, except one character if there was only one character in `alphabet`. `s2` is a string containing the single character from `alphabet` that was removed, if there were multiple characters in `alphabet`. `alphabet` is a set containing the first `k` lowercase English alphabets.
    r = len(s1) // k
    return len(s1) >= n * k, s1[r * k:], s2
    #A boolean indicating whether the length of s1 is greater than or equal to n times k, a substring of s1 starting from index r*k and ending at the end of s1, and the string s2.
#Overall this is what the function does:The function accepts a string `s`, an integer `k`, and an integer `n`. It filters `s` to keep only characters from the first `k` lowercase English alphabets, removing one character if there's only one unique character in those alphabets. It then checks if the filtered string `s1` is at least `n` times `k` characters long. If so, it returns `True`, a substring of `s1` starting from the position `r*k` (where `r` is the smallest integer such that `r*k` is greater than or equal to the length of `s1`), and the string `s2` which contains the removed character. Otherwise, it returns `False`, the same substring, and the same `s2`.

