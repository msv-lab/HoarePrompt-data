#State of the program right berfore the function call: n is a positive integer representing the length of the text. The text consists of n words separated by single spaces, where each word contains only small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: n is a positive integer, l is not empty, m is the maximum number of uppercase letters in any word in the text, i is the last word in the list l, s is the total number of uppercase letters in the word represented by i
    print(m)
#Overall this is what the function does:The function `func` processes a text consisting of n words separated by single spaces, where each word contains only small and capital Latin letters. It calculates the maximum number of uppercase letters in any word in the text and prints this value. The function does not accept any parameters.

