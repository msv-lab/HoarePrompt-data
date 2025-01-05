#State of the program right berfore the function call: n is a positive integer representing the length of the text, and the text consists of n words separated by single spaces, each word containing only small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: `m` is equal to the maximum value between the total number of uppercase characters in all elements of `l` and the previous value of `m`. `s` is the total number of uppercase characters in all elements of `l`, `l` has at least one element, `i` has at least one element.
    print(m)
#Overall this is what the function does:The function `func` processes a text input consisting of n words separated by single spaces, where each word contains only small and capital Latin letters. It iterates through each word to count the number of uppercase characters in that word, then finds the maximum count of uppercase characters across all words. Finally, it prints out the maximum count of uppercase characters found. The function does not accept any parameters and does not return any value explicitly.

