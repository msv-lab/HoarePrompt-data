#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the second input is a string of single-space separated words consisting of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 200; `m` is the maximum count of uppercase letters found in any string in `l`; `l` is a list of strings; `i` is the last string in `l`, and `s` is the count of uppercase letters in `i`.
    print(m)
#Overall this is what the function does:The function accepts a string of space-separated words, counts the number of uppercase letters in each word, and prints the maximum count of uppercase letters found in any single word. It does not utilize the integer `n` in its logic and does not validate the input, meaning it assumes that valid input is always provided.

