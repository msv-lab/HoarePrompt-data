#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the second line of input contains a text of single-space separated words consisting only of small and capital Latin letters.
def func():
    raw_input()
    l = raw_input().split()
    m = 0
    for i in l:
        s = 0
        
        for j in i:
            if j.isupper():
                s += 1
        
        m = max(s, m)
        
    #State of the program after the  for loop has been executed: `l` is a non-empty list of strings, `m` is the maximum count of uppercase characters among all strings in `l`.
    print(m)
#Overall this is what the function does:The function processes a string of text consisting of single-space separated words, where each word can contain both lowercase and uppercase Latin letters. It calculates and returns the maximum number of uppercase letters present in any of the words within the string. The function does not utilize the provided integer `n` (1 ≤ n ≤ 200) and instead focuses solely on the text string provided as input.

