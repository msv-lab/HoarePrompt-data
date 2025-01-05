#State of the program right berfore the function call: n is an integer between 1 and 200 (inclusive), and the second input is a string of single-space separated words consisting only of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 200, `m` is the maximum count of uppercase letters in any word of `l`, `l` is a list of words, `i` is not defined, `s` is not defined.
    print(m)
#Overall this is what the function does:The function accepts an integer `n` (between 1 and 200 inclusive) and a string of single-space separated words. It counts the maximum number of uppercase letters in any of the given words and prints this maximum count. However, it does not actually return any value; it only prints the result.

