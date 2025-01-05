#State of the program right berfore the function call: n is a positive integer representing the length of the text. The text consists of n words separated by single spaces, each word containing only small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer representing the length of the text, `m` is the maximum count of uppercase letters in any word of the text, `l` is a non-empty list, `s` is the total count of uppercase letters in the last word of the text
    print(m)
#Overall this is what the function does:The function processes a text input consisting of n words separated by single spaces, where n is a positive integer. Each word in the text contains only small and capital Latin letters. It calculates the maximum count of uppercase letters in any word of the text and prints this count.

