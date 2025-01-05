#State of the program right berfore the function call: n is a non-negative integer representing the length of the text, and the text consists of n words separated by single spaces, containing only small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer representing the length of the text, `text` consists of `n` words separated by single spaces, `l` is a list containing the individual words from the input text, `m` is the maximum number of uppercase characters in any word in the list `l`
    print(m)
#Overall this is what the function does:The function takes a text input consisting of words separated by single spaces, containing only small and capital Latin letters. It then processes the input to find the word with the maximum number of uppercase characters and prints that number.

