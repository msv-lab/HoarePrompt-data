#State of the program right berfore the function call: **Precondition**: 
- The input consists of an integer n (1 ≤ n ≤ 200) representing the length of the text.
- The input consists of a text of single-space separated words s1, s2, ..., si, consisting only of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `m` will be the maximum count of uppercase letters in any string in the list `l`. `l` must have at least one element for the loop to execute. `j` is a string in uppercase. `s` is incremented by 1 for each uppercase letter encountered.
    print(m)
#Overall this is what the function does:Functionality: The function `func` reads an integer `n` representing the length of the text, followed by a text of single-space separated words `s1, s2, ..., si`. It then calculates the maximum count of uppercase letters in any string within the input text and prints this count. The function does not return any value. The function assumes that the input text will contain at least one word.

