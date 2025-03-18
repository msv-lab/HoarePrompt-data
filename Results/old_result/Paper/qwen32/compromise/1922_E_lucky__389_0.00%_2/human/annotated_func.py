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
        
    #State: `t` is an integer such that 1 <= `t` <= 1000, and for each of the `t` test cases, `X` is an integer such that 2 <= `X` <= 10^18; `x` is 0; `subseq_lens` contains the sequence of powers of 2 that were subtracted from `X-1` in descending order; `mx` is the largest power of 2 that was used in the process.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: `t` is an integer such that 1 <= `t` <= 1000, `X` is an integer such that 2 <= `X` <= 10^18, `x` is 0, `subseq_lens` contains the sequence of powers of 2 that were subtracted from `X-1` in descending order, `mx` is the largest power of 2 that was used in the process, and `ansv` is a list consisting of all elements of `subseq_lens` except the first element.
    #
    #Output State:
    print(len(ansv))
    #This is printed: len(ansv) (where len(ansv) is one less than the number of powers of 2 required to sum up to X-1)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: `t` is an integer such that 1 <= `t` <= 1000, `X` is an integer such that 2 <= `X` <= 10^18, `x` is 0, `subseq_lens` contains the sequence of powers of 2 that were subtracted from `X-1` in descending order, `mx` is the largest power of 2 that was used in the process, `ansv` is a list consisting of all elements of `subseq_lens` except the first element, and `i` is `len(ansv) - 1`. The output will be the elements of `ansv` printed in order, separated by spaces.
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function `func_1` processes a single test case where it receives an integer `X` such that 2 <= X <= 10^18. It calculates a sequence of powers of 2 that sum up to X-1 and outputs the count of these powers minus one, followed by the sequence of powers of 2 (excluding the largest power of 2 used).

