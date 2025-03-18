#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers where each integer a_i satisfies 0 ≤ a_i < n. Additionally, the sum of n over all test cases does not exceed 2 · 10^5, and for the given trace a, there exists a suitable string s consisting of lowercase Latin letters a-z.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: `n` is a positive integer (1 ≤ n ≤ 2 · 10^5), `a` is a list of n integers where each integer a_i satisfies 0 ≤ a_i < n, `s` is a string of length n, `char_count` is a list of 26 integers where each integer represents the count of the corresponding character from 'a' to 'z' that has been added to `s`.
    return s
    #The program returns the string `s` of length `n`, where `n` is a positive integer between 1 and 200,000, and `s` is composed of characters from 'a' to 'z'. The exact composition of `s` is determined by the counts stored in the list `char_count`, which contains 26 integers representing the count of each character from 'a' to 'z' in `s`.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers, where each integer `a_i` satisfies `0 ≤ a_i < n`. It returns a string `s` of length `n` composed of characters from 'a' to 'z'. The characters in `s` are determined such that for each integer `a_i` in the list `a`, the function appends the first character from 'a' to 'z' whose current count in `s` matches `a_i`. The final string `s` will have the characters distributed according to the values in `a`.

