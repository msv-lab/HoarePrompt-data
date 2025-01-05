#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the text is a single line of single-space separated words consisting only of small and capital Latin letters, with the total length equal to n.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 200, `text` is the input string, `l` is a list of strings derived from `text`, `m` is the maximum count of uppercase letters found in any string in `l`.
    print(m)
#Overall this is what the function does:The function reads a line of text input, counts the number of uppercase letters in each word, and prints the maximum count of uppercase letters found in any single word.

