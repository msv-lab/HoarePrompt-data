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
    #State: `t` is an integer such that 1 <= t <= 1000, and for each of the `t` test cases, `X` is an integer such that 2 <= X <= 10^18; `x` is an input integer that is not equal to 2; `subseq_lens` is an empty list; `mx` is 0.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, for each of the `t` test cases, `X` is an integer such that 2 <= X <= 10^18, `x` is 0, `subseq_lens` is a list of integers representing the powers of 2 subtracted from `X` in descending order, and `mx` is the maximum integer in `subseq_lens`.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: `t` is an integer such that 1 <= t <= 1000, `X` is an integer such that 2 <= X <= 10^18, `x` is 0, `subseq_lens` is a list of integers representing the powers of 2 subtracted from `X` in descending order, `mx` is the maximum integer in `subseq_lens`, `ansv` is a list of integers from 0 to `mx - 1` followed by all elements of `subseq_lens` from the second element to the last element.
    print(len(ansv))
    #This is printed: len(ansv) (where len(ansv) is the length of the list ansv constructed as described)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: the loop has printed all elements of `ansv` and the variables `t`, `X`, `x`, `subseq_lens`, `mx` remain unchanged.
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function reads an integer input `x`, processes it to determine a sequence of powers of 2 that sum up to `x`, and then prints the length of a derived sequence followed by the elements of that sequence. If the input is 2, it directly prints 1 and 0.

