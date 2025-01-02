#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the second line of input is a string consisting of single-space separated words where each word is made up of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 200, `l` is a non-empty list of strings, `m` is the maximum count of uppercase characters found in any string within the list `l`.
    print(m)
#Overall this is what the function does:The function processes an input string consisting of single-space separated words, where each word contains small and capital Latin letters. It counts the number of uppercase characters in each word and determines the maximum count among all words. The function then prints this maximum count. The function accepts no explicit parameters but relies on user input for the integer `n` (though `n` is not used in the function) and the input string. The final state of the program after the function concludes is that the maximum count of uppercase characters in any word within the input string is printed. Potential edge cases include empty strings or strings with no uppercase characters, in which case the output will be 0.

