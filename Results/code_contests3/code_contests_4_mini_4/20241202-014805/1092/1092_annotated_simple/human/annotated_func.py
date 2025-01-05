#State of the program right berfore the function call: n is an integer (1 ≤ n ≤ 200), and the second line contains a string of single-space separated words consisting only of small and capital Latin letters, with a total length of n characters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer (1 ≤ n ≤ 200), `m` is the maximum count of uppercase characters found in any word in the list `l`, `l` is a list of words, and `i` is the last word in the list.
    print(m)
#Overall this is what the function does:The function accepts a string of single-space separated words, counts the number of uppercase letters in each word, and prints the maximum count of uppercase letters found in any of the words. It does not return any value and does not enforce the input length constraint based on `n`.

