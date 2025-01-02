#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the second line of input contains a text of single-space separated words consisting only of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `total` is 0, `n` is an integer such that \(1 \leq n \leq 200\), `l` is a list of strings derived from the input line, `m` is the maximum count of uppercase characters found in any string within `l`.
    print(m)
#Overall this is what the function does:The function reads two lines of input where the first line is ignored, the second line is a string of single-space separated words consisting of small and capital Latin letters. It then iterates through each word in the string, counts the number of uppercase letters in each word, and determines the maximum count among all words. Finally, it prints the maximum count of uppercase letters found in any word. The function does not accept any parameters and does not return a value.

