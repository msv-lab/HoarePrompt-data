#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^{18}.
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
        
    #State: mx is the maximum value of i found during the loop, subseq_lens is a list containing all the values of i that satisfy the conditions within the loop.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `mx` is the maximum value of `i` found during the loop; `subseq_lens` is a list containing all the values of `i` that satisfy the conditions within the loop; `ansv` is a list of integers ranging from 0 to `mx-1`, with each integer appended once from `subseq_lens` starting from index 1 to the end.
    print(len(ansv))
    #This is printed: mx + len(subseq_lens)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: The output state remains unchanged as no variables `mx`, `subseq_lens`, or `ansv` are modified within the loop. The loop simply prints the elements of `ansv` one by one.
    print()
    #This is printed: each element of the list `ansv` in sequence
#Overall this is what the function does:The function processes a single test case where `t` is a positive integer within the range 1 to 1000, and `X` is an integer within the range 2 to \(10^{18}\). It calculates a list of integers ranging from 0 to `mx-1`, where `mx` is the maximum value of `i` found during a specific loop. Additionally, it appends elements from another list `subseq_lens` to this list. Finally, it prints the length of the resulting list followed by its elements in sequence.

