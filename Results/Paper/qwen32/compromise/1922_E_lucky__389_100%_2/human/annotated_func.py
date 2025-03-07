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
        #The program returns nothing.
    #State: `t` is an integer such that 1 <= t <= 1000, and for each of the t test cases, X is an integer such that 2 <= X <= 10^18; `x` is an input integer and `x` is not equal to 2; `subseq_lens` is an empty list; `mx` is 0.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, and for each of the t test cases, `X` is an integer such that 2 <= X <= 10^18; `x` is 0; `subseq_lens` is a list containing the lengths of all subsequences of powers of 2 that sum up to the original `X`; `mx` is the maximum length of these subsequences.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, X is an integer such that 2 <= X <= 10^18; x is 0; subseq_lens is a list containing the lengths of all subsequences of powers of 2 that sum up to the original X; mx is the maximum length of these subsequences; ansv is a list containing elements from subseq_lens[1] to subseq_lens[len(subseq_lens) - 1].
    print(len(ansv))
    #This is printed: len(ansv) (where len(ansv) is the length of subseq_lens minus 1)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: the elements of `ansv` printed in order, each followed by a space.
    print()
    #This is printed: \n
#Overall this is what the function does:The function `func_1` reads an integer `X` from the input, where `X` is at least 2. It calculates the lengths of subsequences of powers of 2 that sum up to `X` and prints the number of such subsequences minus one, followed by the lengths of these subsequences (excluding the first one). If `X` is 2, it directly prints 1 and 0. The function does not return any value.

