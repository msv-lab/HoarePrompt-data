#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200. The text consists of n single-space separated words, each word consists of small and capital Latin letters.**
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
        
    #State of the program after the  for loop has been executed: Output State: `n` is an integer within the range 1 to 200, `l` is a list containing words from the input, `m` is the maximum number of uppercase letters in any word in `l`, `s` is the total number of uppercase letters in all elements of `l`, `i` is an empty iterable object.
    print(m)
#Overall this is what the function does:The function `func` reads an integer `n` and a sequence of `n` words. It then calculates the maximum number of uppercase letters in any word from the input sequence and prints this value. The function does not accept any parameters and does not return any value.

