#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, X is an integer such that 2 <= X <= 10^18.
def func_1():
    x = int(input())
    subseq_lens = []
    mx = 0
    if (x == 2) :
        print(1)
        #This is printed: 1
        print(0)
        #This is printed: 0
        return
        #The program does not return any value.
    #State: `t` is an integer such that 1 <= t <= 1000, and for each of the t test cases, X is an integer such that 2 <= X <= 10^18; `x` is the integer value read from input, and `x` is not equal to 2; `subseq_lens` is an empty list; `mx` is 0.
    while x != 0:
        i = 0
        
        while 2 ** i <= x:
            i += 1
        
        if i == 0:
            break
        else:
            subseq_lens.append(i - 1)
            x -= 2 ** (i - 1)
            mx = max(mx, i - 1)
        
    #State: x is 0, subseq_lens contains the exponents of the powers of 2 subtracted from the initial x, and mx is the maximum of these exponents.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: `x` is 0, `subseq_lens` contains the exponents of the powers of 2 subtracted from the initial `x`, `mx` is the maximum of these exponents, `ansv` is a list of integers from 0 to `mx - 1` with additional elements from `subseq_lens` starting from index 1 appended to it.
    print(len(ansv))
    #This is printed: 0
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: x is 0, subseq_lens is [], mx is 0, ansv is [].
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function `func_1` reads an integer `x` from the input, computes a sequence of exponents related to the powers of 2 that sum up to `x`, and prints the length of this sequence followed by the sequence itself. If `x` is 2, it directly prints 1 and 0. The function does not return any value.

