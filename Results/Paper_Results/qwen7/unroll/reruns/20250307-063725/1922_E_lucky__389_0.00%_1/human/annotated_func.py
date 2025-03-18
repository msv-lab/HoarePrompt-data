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
        
    #State: mx is the maximum value of i found during the loop, subseq_lens is a list containing all the values of i where i was not 0, and x is 0.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `mx` is the maximum value of `i` found during the loop, `subseq_lens` is a list containing all the values of `i` where `i` was not 0, `ansv` is a list containing all the values of `subseq_lens` from index 1 to the end, and `x` is 0.
    print(len(ansv))
    #This is printed: len(subseq_lens) - 1 (if subseq_lens starts with 0) or len(subseq_lens) (otherwise)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: `mx` is the maximum value of `i` found during the loop, `subseq_lens` is a list containing all the values of `i` where `i` was not 0, `ansv` is a list containing all the values of `subseq_lens` from index 1 to the end, and `x` is 0. The loop prints each element of `ansv` starting from index 1 to the end, separated by spaces.
    print()
    #This is printed: the values in ansv from index 1 to the end, separated by spaces
#Overall this is what the function does:The function processes an integer input \(X\) (where \(2 \leq X \leq 10^{18}\)) to generate a sequence of integers based on certain conditions. It calculates the maximum value \(i\) for which \(2^{i+1} \leq X + 1\), and constructs a list `subseq_lens` containing all such values of \(i\). Then, it creates another list `ansv` that combines the maximum value \(i\) and the elements of `subseq_lens` starting from the second element. Finally, it prints the length of `ansv` followed by its elements, each separated by a space.

