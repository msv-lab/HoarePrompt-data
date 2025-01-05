#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the text is a single line of single-space separated words consisting only of small and capital Latin letters with a total length of n.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 200; `m` is the maximum count of uppercase letters in any word from the list `l`; `l` is a list of words; `i` is the last word in the list `l`; `s` is the count of uppercase letters in the last word `i`.
    print(m)
#Overall this is what the function does:The function accepts an integer `n` and a line of words, counts the maximum number of uppercase letters in any word, and prints this maximum count. It does not validate the input or handle empty cases, which could lead to incorrect outputs.

