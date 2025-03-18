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
        
    #State: `s` is a string of length `n` where each character is determined by the first occurrence of the value `a[i]` in `char_count` (converted to a corresponding lowercase letter), and `char_count` is updated to reflect the counts of these characters. The list `a` and the integer `n` remain unchanged.
    return s
    #The program returns the string `s` of length `n`, where each character in `s` is determined by the first occurrence of the value `a[i]` in `char_count` (converted to a corresponding lowercase letter). The list `a` and the integer `n` remain unchanged.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers. It returns a string `s` of length `n`, where each character in `s` is determined by the first occurrence of the value `a[i]` in a list `char_count` of 26 zeros, which is then converted to a corresponding lowercase letter. The input parameters `n` and `a` remain unchanged.

