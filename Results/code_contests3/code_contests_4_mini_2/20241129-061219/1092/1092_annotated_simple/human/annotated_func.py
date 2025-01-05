#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the input text consists of single-space separated words containing only small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 200; `m` is the maximum number of uppercase characters found in any string within the list `l`; `l` is a list of strings; `i` is the last string in the list `l` processed; `s` is the count of uppercase letters in the last string `i`.
    print(m)
#Overall this is what the function does:The function reads a line of space-separated words from input, counts the maximum number of uppercase letters in any word, and prints this maximum count. If no uppercase letters are found, it will print `0`. The function does not handle cases where the input is empty or invalid.

