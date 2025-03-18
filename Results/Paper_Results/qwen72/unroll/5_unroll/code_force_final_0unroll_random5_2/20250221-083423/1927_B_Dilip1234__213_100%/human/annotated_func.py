#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 2 \cdot 10^5, and a is a list of n integers where 0 <= a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: `n` remains a positive integer such that 1 <= n <= 2 \cdot 10^5, `a` remains a list of n integers where 0 <= a_i < n, `s` is a string of length n, `char_count` is a list of 26 integers where each element represents the number of times the corresponding character (from 'a' to 'z') has been appended to `s`.
    return s
    #The program returns a string `s` of length `n`, where `n` is a positive integer such that 1 <= n <= 200,000. The string `s` is composed of characters that have been appended based on the counts in the `char_count` list, which tracks the number of times each character from 'a' to 'z' appears in `s`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers, where each integer `a_i` is in the range 0 to `n-1`. It returns a string `s` of length `n`, where each character in `s` is determined by the first character (from 'a' to 'z') whose count in the `char_count` list matches the current integer in `a`. The `char_count` list tracks the number of times each character from 'a' to 'z' has been appended to `s`. After the function concludes, `n` and `a` remain unchanged, and `s` is a string of length `n` composed of characters from 'a' to 'z'.

