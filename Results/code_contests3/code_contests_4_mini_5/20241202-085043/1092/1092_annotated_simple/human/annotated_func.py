#State of the program right berfore the function call: n is an integer between 1 and 200 (inclusive), and the second line is a string of single-space separated words consisting of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 200, `m` is the maximum count of uppercase characters found in any word in `l`, `l` is a list of words, and `i` is the last word in the list processed (which could be an empty string), and `s` is the count of uppercase characters in `i` at that moment.
    print(m)
#Overall this is what the function does:The function reads a list of words from input, counts the number of uppercase letters in each word, and returns the maximum count of uppercase letters found in any single word. It does not explicitly utilize the parameter `n`, which is mentioned in the annotations, and it does not handle cases where the input string could be empty or contain only whitespace.

