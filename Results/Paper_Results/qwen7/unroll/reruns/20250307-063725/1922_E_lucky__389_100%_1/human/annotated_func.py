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
    #State: `mx` is 0, `t` is a positive integer such that 1 ≤ t ≤ 1000, `x` is an integer such that 2 ≤ x ≤ 10^18, `subseq_lens` is an empty list, and x is not equal to 2
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
        
    #State: `mx` is the maximum value of `i - 1` where `2
    ansv = [i for i in range(mx)]
    for i in range(1, len(subseq_lens)):
        ansv.append(subseq_lens[i])
        
    #State: Output State: `mx` is the maximum value of `i - 1` where `2 < i <= mx`; `ansv` is a list containing integers from 0 to `len(subseq_lens)-2`.
    print(len(ansv))
    #This is printed: len(subseq_lens) - 1
    for i in range(len(ansv)):
        print(ansv[i], end=' ')
        
    #State: the list `ansv` is printed with each element separated by a space.
    print()
    #This is printed: 
#Overall this is what the function does:The function reads an integer `x` from the user. If `x` is 2, it prints 1 followed by 0 and returns. Otherwise, it calculates a sequence of integers based on certain conditions and prints the length of this sequence followed by its elements, each separated by a space. The function does not return any value.

