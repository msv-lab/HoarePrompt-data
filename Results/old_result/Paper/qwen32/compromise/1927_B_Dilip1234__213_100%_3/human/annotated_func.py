#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, for each test case n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5, `a` is a list of `n` integers where 0 ≤ a_i < n, `s` is a string containing `n` characters, `char_count` is a list of 26 integers where each entry reflects the number of times the corresponding character was added to `s`, `i` is `n`.
    return s
    #The program returns the string `s` containing `n` characters.
#Overall this is what the function does:The function `func_1` generates a string `s` of `n` characters based on the input list `a` where each element in `a` specifies the position at which the next unused character from 'a' to 'z' should be placed in the string. The function returns this generated string `s`.

