#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5) representing the length of the lost string, and a is a list of n integers (0 ≤ a_i < n) representing the trace of the string. It is guaranteed that the sum of n over all test cases does not exceed 2 · 10^5 and that for the given trace, there exists a suitable string s.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: `s` is a string of length `n` where each character's count in `s` matches the values in `a`; `char_count` is a list of 26 integers reflecting the counts of each character in `s`.
    return s
    #The program returns the string `s` which is a string of length `n` where each character's count in `s` matches the values in `a`.
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer representing the length of the desired string, and `a`, a list of `n` integers where each integer `a_i` indicates the count of the character at position `i` in the string `s`. The function returns a string `s` of length `n` such that the count of each character in `s` matches the values specified in the list `a`.

