#State of the program right berfore the function call: n is an integer in the range 1 to 200 (1 ≤ n ≤ 200), and the text is a single line containing single-space separated words consisting only of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is in the range 1 to 200, `text` is a non-empty string, `l` is a list of words with at least 1 word, `m` is the maximum number of uppercase letters found in any single word from `l`, and `s` is the count of uppercase characters in the last word `i` processed.
    print(m)
#Overall this is what the function does:The function accepts an integer `n` (from 1 to 200) and a string `text` that contains single-space separated words. It counts the maximum number of uppercase letters found in any single word from `text` and prints this maximum count. If there are no uppercase letters in any word, it will print 0. The function does not return any value; it only prints the result.

