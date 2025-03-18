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
        
    #State: After the loop executes all the iterations, `s` will be an empty string, `s1` will contain all characters from the original string `s` that were in the set `alphabet`, and `s2` will be a string containing the last character of `s` if it was in `alphabet` and `len(alphabet) == 1` during any iteration. `alphabet` will be a set containing the first `k` lowercase English alphabets.
    r = len(s1) // k
    return len(s1) >= n * k, s1[r * k:], s2
    #The program returns a boolean indicating whether the length of `s1` is greater than or equal to `n * k`, a substring of `s1` starting from index `r * k` to the end, and the string `s2` which contains the last character of `s` if it was in `alphabet` and `len(alphabet) == 1` during any iteration.
#Overall this is what the function does:The function `func_1` accepts three parameters: a string `s`, a positive integer `k`, and another positive integer `n`. It processes the string `s` by removing characters that are not part of the first `k` lowercase English alphabets, and it keeps track of the last character of `s` if it was one of those `k` alphabets. After processing, the function returns a boolean indicating whether the length of a specific substring of `s1` (which contains remaining valid characters) is at least `n * k`, a substring of `s1` starting from index `r * k` to the end, and the string `s2` which contains the last character of `s` if it was one of the first `k` alphabets.

