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
        
    #State: `x` is 0, `subseq_lens` is a list of integers representing the powers of 2 used, and `mx` is the maximum value in `subseq_lens`.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: - `x` remains 0.
    #- `subseq_lens` remains unchanged.
    #- `mx` remains unchanged.
    #- `ansv` will now include its original elements (0 to `mx - 1`) followed by the elements of `subseq_lens` starting from the second element.
    #
    #Given the format, the output state is:
    #
    #Output State:
    print(len(ansv))
    #This is printed: mx + len(subseq_lens) - 1 (where mx is the original length of ansv and len(subseq_lens) is the length of the subseq_lens list)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: `x` remains 0. `subseq_lens` remains unchanged. `mx` remains unchanged. `ansv` remains unchanged.
    print()
    #This is printed: (newline)
#Overall this is what the function does:The function `func_1` reads an integer `X` from the input, computes a sequence based on the powers of 2 that can be subtracted from `X` until `X` becomes zero, and then outputs the length and the elements of this sequence. The sequence is constructed by first including all integers from 0 to the maximum power of 2 used minus one, followed by the powers of 2 used in the sequence, excluding the first one.

