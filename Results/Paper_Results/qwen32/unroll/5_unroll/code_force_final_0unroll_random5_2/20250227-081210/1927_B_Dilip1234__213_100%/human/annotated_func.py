#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where 0 ≤ a_i < n. The sum of n over all test cases does not exceed 2 \cdot 10^5. It is guaranteed that for the given trace, there exists a suitable string s consisting of lowercase Latin letters a-z.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: `s` is a string of length `n` constructed based on the values in `a` and `char_count` reflects the frequency of each character in `s`. The values of `t`, `n`, and `a` remain unchanged.
    return s
    #The program returns the string `s` of length `n` constructed based on the values in `a` and `char_count` reflects the frequency of each character in `s`.
#Overall this is what the function does:The function `func_1` takes an integer `n` and a list `a` of `n` integers, and returns a string `s` of length `n` composed of lowercase Latin letters. The string `s` is constructed such that the frequency of each character in `s` corresponds to the values specified in the list `a`.

