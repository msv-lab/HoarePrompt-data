#State of the program right berfore the function call: n is a positive integer representing the length of the text. The text consists of n single-space separated words, each word consisting of small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer representing the length of the text, `l` is a non-empty list, `m` is the maximum number of uppercase characters in any word in the list `l`
    print(m)
#Overall this is what the function does:The function accepts no parameters and reads input to process a text consisting of n single-space separated words, where each word contains small and capital Latin letters. It then calculates and prints the maximum number of uppercase characters in any word within the text.

