#State of the program right berfore the function call: n is an integer between 1 and 200 inclusive, and the second line contains a string of single-space separated words consisting only of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 1 and 200 inclusive; `m` is the maximum number of uppercase characters found in any word in the list `l`; `l` is a list of words obtained from the input string; `i` is the last word in the list (if the list is not empty); `s` is the count of uppercase characters in the last word `i`.
    print(m)
#Overall this is what the function does:The function reads a line of input containing a string of space-separated words and calculates the maximum number of uppercase letters found in any of those words. It then prints this maximum count. The parameter `n` is not directly used in any computations within the function, and the function does not return any values; it only prints the result.

