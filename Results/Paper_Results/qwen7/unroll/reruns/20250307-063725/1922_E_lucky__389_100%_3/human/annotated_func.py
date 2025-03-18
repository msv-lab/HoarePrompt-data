#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^18.
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
        
    #State: mx is the maximum value of \(i-1\) found during the loop, and subseq_lens is a list containing all values of \(i-1\) found during the loop.
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `mx` is the maximum value of \(i-1\) found during the loop, `subseq_lens` is a list containing all values of \(i-1\) found during the loop, `ansv` is a list of integers ranging from 0 to `mx-1`, with each integer appearing `len(subseq_lens) - 1` times.
    print(len(ansv))
    #This is printed: mx \* (len(subseq_lens) - 1)
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: The loop will print each integer from 0 to `mx-1`, each appearing `len(subseq_lens) - 1` times, separated by spaces.
    print()
    #This is printed: nothing (the loop will print each integer from 0 to mx-1, each appearing len(subseq_lens) - 1 times, separated by spaces)
#Overall this is what the function does:The function processes an input integer \(x\) and calculates a sequence based on certain conditions. It then prints the length of this sequence followed by the sequence itself, where each integer from 0 to \(mx-1\) appears \(len(subseq\_lens) - 1\) times. The function does not return any value.

