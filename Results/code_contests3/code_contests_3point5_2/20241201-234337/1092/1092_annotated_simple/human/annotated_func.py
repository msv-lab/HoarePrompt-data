#State of the program right berfore the function call: n is an integer such that 1 <= n <= 200. The text consists of n single-space separated words, where each word consists of small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 200, `l` is a list containing n words, `i` is the last word in the list `l`, `m` is the maximum value between the total count of uppercase characters in all words in the list and 0, `s` is the total count of uppercase characters in all words in the list
    print(m)
#Overall this is what the function does:The function `func` reads an integer `n` as input and then reads `n` words. It calculates the maximum count of uppercase letters in any single word among the `n` words and prints this maximum count. The function does not accept any parameters and does not return any value.

