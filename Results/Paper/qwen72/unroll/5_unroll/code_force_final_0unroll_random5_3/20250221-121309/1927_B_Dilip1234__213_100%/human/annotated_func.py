#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers (0 ≤ a_i < n) representing the trace of the string. The sum of n over all test cases does not exceed 2 · 10^5, and it is guaranteed that for the given trace, there exists a suitable string s.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: `n` is a positive integer (1 ≤ n ≤ 2 · 10^5), `a` is a list of n integers (0 ≤ a_i < n) representing the trace of the string, `s` is a string of length n where each character is determined by the trace `a` and the `char_count` array, `char_count` is a list of 26 integers where each element represents the number of times the corresponding character (from 'a' to 'z') has been added to `s`.
    return s
    #The program returns the string `s` of length `n`, where each character in `s` is determined by the trace `a` and the `char_count` array. The `char_count` array represents the number of times each character from 'a' to 'z' has been added to `s`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers. It returns a string `s` of length `n` where each character in `s` is determined by the trace `a` and the count of each character from 'a' to 'z' that has been added to `s`. The `char_count` array, which is used internally, tracks the number of times each character from 'a' to 'z' has been added to `s`. After the function concludes, the input variables `n` and `a` remain unchanged, and the string `s` is the final output.

