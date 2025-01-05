#State of the program right berfore the function call: n is a positive integer representing the length of the text. The text consists of n single-space separated words containing only small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `l` is a list containing words from the text, `m` is the maximum count of uppercase letters in any word in the list `l`
    print(m)
#Overall this is what the function does:The function `func` reads input text that consists of n single-space separated words containing only small and capital Latin letters, where n is a positive integer representing the length of the text. It then calculates the maximum count of uppercase letters in any word within the text and prints this count. The function does not explicitly accept any parameters but relies on the input text provided within the function body.

