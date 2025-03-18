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
        
    #State: mx is the maximum value of i found during the loop, subseq_lens is a list containing all values of i found during the loop.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: `mx` is the maximum value of `i` found during the loop; `subseq_lens` is a list containing all values of `i` found during the loop; `ansv` is a list containing all integers from 0 to `len(subseq_lens)-2`.
    print(len(ansv))
    #This is printed: len(subseq_lens) - 1
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: mx is the maximum value of i found during the loop; subseq_lens is a list containing all values of i found during the loop; ansv is a list containing all integers from 0 to len(subseq_lens)-2, printed as 0 1 2 ... (len(subseq_lens)-2) separated by spaces.
    print()
    #This is printed: Output: (an empty line)
#Overall this is what the function does:The function processes a single test case where `t` is a positive integer within the range 1 to 1000, and `X` is an integer within the range 2 to 10^18. It calculates a sequence of integers based on certain conditions and prints the length of this sequence followed by the sequence itself. The function does not return any value but outputs the result directly.

