#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 2 · 10^5), and a is a list of n integers (0 ≤ a_i < n) representing the trace of the string.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: `n` is a positive integer (1 ≤ n ≤ 2 · 10^5), `a` is a list of n integers (0 ≤ a_i < n), `s` is a string of n characters, `char_count` is a list of 26 integers where each integer represents the count of the corresponding character (from 'a' to 'z') in the string `s`.
    return s
    #The program returns the string `s` which is a string of n characters, where n is a positive integer between 1 and 200,000.
#Overall this is what the function does:The function `func_1` accepts a positive integer `n` and a list `a` of `n` integers, and returns a string `s` of `n` characters. The string `s` is constructed such that each character in `s` corresponds to an integer in `a`, where the integer represents the count of that character in `s` up to the current position. The function ensures that the characters are chosen from 'a' to 'z' and that the counts are updated correctly as the string is built. After the function concludes, the final state of the program includes the returned string `s` which is a valid reconstruction based on the trace in `a`.

