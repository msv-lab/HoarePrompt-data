#State of the program right berfore the function call: n is an integer between 1 and 200 (inclusive) representing the length of the text, and the text is a string of single-space separated words consisting only of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 200, `m` is the maximum count of uppercase letters found in any string of `l`, `l` is a list of strings.
    print(m)
#Overall this is what the function does:The function reads an integer `n` and a string of single-space separated words from input, counts the maximum number of uppercase letters in any word, and prints this maximum count. It does not validate the length of the input string against `n` and does not return a value.

