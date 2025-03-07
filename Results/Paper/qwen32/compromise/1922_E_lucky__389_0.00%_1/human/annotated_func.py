#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, X is an integer such that 2 <= X <= 10^18.
def func_1():
    x = int(input())
    x -= 1
    subseq_lens = []
    mx = 0
    while x != 0:
        i = 0
        
        while 2 ** (i + 1) <= x + 1:
            i += 1
        
        if i == 0:
            break
        else:
            subseq_lens.append(i)
            x -= 2 ** i - 1
            mx = max(mx, i)
        
    #State: t is an integer such that 1 <= t <= 1000, x is 0, subseq_lens is [3, 3, 4], and mx is 4.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: t is an integer such that 1 <= t <= 1000, x is 0, subseq_lens is [3, 3, 4], mx is 4, ansv is [0, 1, 2, 3, 4, 4]
    print(len(ansv))
    #This is printed: 6
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: t is an integer such that 1 <= t <= 1000, x is 0, subseq_lens is [3, 3, 4], mx is 4, ansv is [0, 1, 2, 3, 4, 4], i is 6
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function `func_1` reads an integer `X` from the input, processes it to determine a sequence of subsequence lengths, and then outputs the length of a derived list `ansv` followed by the elements of `ansv`. The function does not accept any parameters and does not return any values explicitly; instead, it prints the results directly.

