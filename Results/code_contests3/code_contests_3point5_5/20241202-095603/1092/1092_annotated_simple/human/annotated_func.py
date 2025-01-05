#State of the program right berfore the function call: n is an integer such that 1 <= n <= 200. The text contains n words separated by single spaces, consisting of small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= n <= 200, `l` is a list of n words with at least 1 word, `m` is the maximum value between the total number of uppercase characters in all words in list `l` and the initial value of `m`, `i` is the last word in list `l`, `s` is the total number of uppercase characters in the word `i`
    print(m)
#Overall this is what the function does:The function `func` processes `n` words separated by single spaces, consisting of small and capital Latin letters. It iterates over each word to count the number of uppercase characters in that word and keeps track of the maximum count found among all words. Finally, it prints the maximum count of uppercase characters found in any single word. The function does not accept any parameters and does not return any values.

