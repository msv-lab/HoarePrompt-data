#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200, and the input text consists of a single line of words separated by single spaces, containing only small and capital Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 200, `l` is a list of words, `m` is the maximum count of uppercase letters found in any word in `l`.
    print(m)
#Overall this is what the function does:The function accepts no parameters but processes a line of input that contains words consisting of Latin letters. It counts the maximum number of uppercase letters found in any single word of the input and prints this maximum count. There is no explicit return value, and the function assumes the input will always conform to the expected format, without handling any potential input errors or variations.

