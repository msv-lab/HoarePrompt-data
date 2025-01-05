#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200. The text consists of n single-space separated words, each word containing only small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `l` is a list containing n words, `m` is the maximum count of uppercase characters in any word in list `l`, `i` is the last word in list `l`, `s` is the total count of uppercase characters in all words in list `l`
    print(m)
#Overall this is what the function does:The function `func` reads an integer `n` within the range of 1 to 200. It then reads a text consisting of `n` single-space separated words, where each word contains only small and capital Latin letters. For each word, the function counts the number of uppercase letters and determines the maximum count of uppercase characters in any word. Finally, it prints the maximum count of uppercase characters found in any word.

