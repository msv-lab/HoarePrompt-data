#State of the program right berfore the function call: n is an integer between 1 and 200 inclusive, and the second input is a string of single-space separated words consisting only of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 200 inclusive, `m` is the maximum count of uppercase characters found in any word in the list `l`, `l` is a list of words, `i` is the last word in the list `l`, `s` is the count of uppercase characters in `i`, `j` is the last character in the string `i`.
    print(m)
#Overall this is what the function does:The function accepts an integer `n` (though it is not used in the implementation) and reads a string of single-space separated words from the input. It counts the maximum number of uppercase letters found in any word from the input string and prints that maximum count. The function does not handle cases where the input is empty or contains no uppercase letters, which could lead to misleading output since the maximum `m` will default to 0 if no uppercase letters are found.

