#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^{18}.
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
        #The program returns None
    #State: `mx` is 0, `t` is a positive integer such that 1 ≤ t ≤ 1000, `x` is an input integer, `subseq_lens` is an empty list, and `x` is not equal to 2
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
        
    #State: mx is the maximum value of \(i-1\) found during the loop, and subseq_lens is a list of all \(i-1\) values found during the loop executions.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `mx` is the maximum value of \(i-1\) found during the loop, `subseq_lens` is a list of all \(i-1\) values found during the loop executions, `ansv` is a list containing all elements from `subseq_lens` starting from index 1 to the end.
    print(len(ansv))
    #This is printed: n - 1 (where n is the length of subseq_lens)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: The output state remains unchanged because the loop does not modify any variables. The loop only prints the elements of `ansv` starting from index 1 to the end, but it does not change the values of `mx`, `subseq_lens`, or `ansv`.
    print()
    #This is printed: Output:
#Overall this is what the function does:The function processes an input integer \(x\) and calculates a sequence based on the binary representation of \(x\). It then prints the length of this sequence followed by its elements. If the input \(x\) is 2, it directly prints 1 and 0 and returns. Otherwise, it finds the maximum length of the binary prefix that can be subtracted from \(x\) repeatedly, constructs a sequence based on these lengths, and prints the sequence along with its length. The function does not return any value.

