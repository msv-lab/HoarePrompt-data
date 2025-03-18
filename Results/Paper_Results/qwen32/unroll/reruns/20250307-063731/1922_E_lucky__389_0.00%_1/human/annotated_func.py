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
        
    #State: `t` is unchanged, `X` is unchanged, `subseq_lens` contains the lengths of subsequences, and `mx` is the maximum length of these subsequences.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: `t` is unchanged, `X` is unchanged, `subseq_lens` contains the lengths of subsequences, `mx` is the maximum length of these subsequences, `ansv` is a list starting with integers from 0 to `mx - 1` followed by all elements of `subseq_lens` except the first one.
    print(len(ansv))
    #This is printed: mx + (n - 1) (where mx is the maximum length of the subsequences in subseq_lens and n is the total number of elements in subseq_lens)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: `t` is unchanged, `X` is unchanged, `subseq_lens` contains the lengths of subsequences, `mx` is the maximum length of these subsequences, `ansv` is a list starting with integers from 0 to `mx - 1` followed by all elements of `subseq_lens` except the first one.
    print()
    #This is printed: (newline character)
#Overall this is what the function does:The function `func_1` reads an integer `X` from the input, processes it to determine a sequence of subsequence lengths, and then prints the length of a derived list followed by the elements of this list. The input `X` is modified during the process, but the original value is not preserved. The function does not accept any parameters directly; it operates on input read from standard input.

