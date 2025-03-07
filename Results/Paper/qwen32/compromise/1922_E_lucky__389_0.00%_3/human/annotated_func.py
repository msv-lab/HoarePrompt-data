#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, X is an integer such that 2 <= X <= 10^18.
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
        
    #State: t is an integer such that 1 <= t <= 1000, X is an integer such that 2 <= X <= 10^18, x is 0, subseq_lens is a list of integers representing the significant bits of the original x + 1, mx is the maximum value of i encountered during the loop.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: `t` is an integer such that 1 <= t <= 1000, `X` is an integer such that 2 <= X <= 10^18, `x` is 0, `subseq_lens` is a list of integers with at least `len(subseq_lens)` elements, `mx` is `len(subseq_lens) - 1`, `ansv` is a list of integers starting from `subseq_lens[1]` to `subseq_lens[len(subseq_lens) - 1]`.
    print(len(ansv))
    #This is printed: len(subseq_lens) - 1 (where len(subseq_lens) is the length of the subseq_lens list)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: `t` is an integer such that 1 <= t <= 1000, `X` is an integer such that 2 <= X <= 10^18, `x` is 0, `subseq_lens` is a list of integers with at least `mx + 1` elements, `mx` is the length of `ansv` minus 1, `ansv` is a list of integers starting from `subseq_lens[1]` to `subseq_lens[mx]`, `i` is `mx`.
    print()
    #This is printed: (an empty line)
#Overall this is what the function does:The function `func_1` reads an integer `X` from the input, processes it to determine a sequence of significant bit positions, and prints the length of this sequence followed by the sequence itself. The input `X` must be an integer such that 2 <= X <= 10^18. The function does not accept a parameter `t` for the number of test cases; instead, it processes a single input value `X`.

