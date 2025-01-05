#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the text is a string of single-space separated words consisting only of small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 200, `m` is the maximum count of uppercase letters found in any word in `l`, `l` is a list of words, and `i` is the last word in the list processed in the loop.
    print(m)
#Overall this is what the function does:The function accepts an integer `n` (with a constraint of 1 ≤ n ≤ 200) and reads a line of input consisting of words. It processes these words to count the number of uppercase letters in each word and returns the maximum count of uppercase letters found in any of those words. The function does not actually take parameters as stated in the annotations, and it does not handle cases where no words are entered (leading to a maximum count of 0).

