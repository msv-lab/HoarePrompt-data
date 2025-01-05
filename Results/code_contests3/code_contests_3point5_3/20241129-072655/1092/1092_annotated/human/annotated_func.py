#State of the program right berfore the function call: n is an integer such that 1 <= n <= 200. The text consists of n words separated by single spaces, each word contains only small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: n is between 1 and 200, l is a list of n words with at least 1 word, m is the maximum value of s among all words in list l, i is the last word in the list, s is the total count of uppercase letters in the last word in list l
    print(m)
#Overall this is what the function does:The function `func` processes a text consisting of n words separated by single spaces, where each word contains only small and capital Latin letters. It calculates the maximum count of uppercase letters in any word within the text and prints this count. The function does not accept any parameters and does not return any value.

