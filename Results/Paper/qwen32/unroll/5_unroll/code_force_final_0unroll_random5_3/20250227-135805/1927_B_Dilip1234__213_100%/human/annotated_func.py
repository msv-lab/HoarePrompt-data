#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5, and a is a list of n integers where each a_i satisfies 0 ≤ a_i < n. Additionally, it is guaranteed that the trace a corresponds to a valid string s consisting of lowercase Latin letters.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: `s` is a string constructed by appending characters according to the values in `a`, and `char_count` is a list where `char_count[j]` is the number of times the character `chr(j + ord('a'))` appears in `s`.
    return s
    #The program returns the string `s` which is constructed by appending characters according to the values in `a`.
#Overall this is what the function does:The function takes an integer `n` and a list `a` of `n` integers as input and returns a string `s` constructed by appending characters according to the values in `a`. Each value in `a` specifies the position at which the next character in the alphabet should appear in the string `s` for the first time.

