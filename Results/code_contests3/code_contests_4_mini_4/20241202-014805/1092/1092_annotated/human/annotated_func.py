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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 200, `m` is the maximum count of uppercase characters in any word in `l`, `l` is a list of words.
    print(m)
#Overall this is what the function does:The function reads a string of single-space separated words and calculates the maximum number of uppercase characters in any of those words. It then prints this maximum count. Note that the function does not use the integer `n` in any way, and there is no handling for edge cases such as empty input.

