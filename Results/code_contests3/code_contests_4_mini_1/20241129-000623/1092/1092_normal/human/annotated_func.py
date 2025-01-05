#State of the program right berfore the function call: n is an integer between 1 and 200 (inclusive), and the second line contains a string of single-space separated words consisting only of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 200, `m` is the maximum count of uppercase letters found in any word in `l`, `l` is a list of words, each `i` is a word in `l`, `s` is the count of uppercase letters in the last word processed.
    print(m)
#Overall this is what the function does:The function accepts a list of words input by the user and returns the maximum count of uppercase letters found in any single word within that list. It does not specifically utilize the integer `n` as described in the annotations, and it does not handle cases where the input may not conform to the expected format (e.g., empty input). The function simply prints the maximum count of uppercase letters and does not return any value.

