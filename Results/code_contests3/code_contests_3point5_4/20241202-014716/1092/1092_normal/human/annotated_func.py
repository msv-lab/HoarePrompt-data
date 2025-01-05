#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200. The text consists of n words separated by single spaces, each word containing only small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: n is an integer such that 1 ≤ n ≤ 200, l is a list containing words, m is the maximum count of uppercase characters in any word in the list, i is the last word in the list, s is the total count of uppercase characters in all words of the list, j is an uppercase character if the loop executes
    print(m)
#Overall this is what the function does:The function `func` reads a text consisting of n words, each word containing only small and capital Latin letters. It then calculates the maximum count of uppercase characters in any word in the text and prints this count. The function does not accept any parameters and does not return any value.

