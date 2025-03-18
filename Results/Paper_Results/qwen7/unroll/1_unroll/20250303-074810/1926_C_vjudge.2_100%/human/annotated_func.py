#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5.
def func():
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: Output State: `pd` is a list of 400001 elements where each element `pd[i]` (for 1 ≤ i ≤ 400000) contains the sum of the digits of all numbers from 1 to i, and `t`, `N`, `n` are unchanged.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: pd is a list of 400001 elements where each element pd[i] (for 1 ≤ i ≤ 400000) contains the sum of the digits of all numbers from 1 to i, t, N, and n are unchanged after the loop executes all iterations. Each time the loop runs, it reads an integer n from input, prints the precomputed sum of digits up to n from the list pd, and does not modify pd or any other variables outside the loop.
#Overall this is what the function does:The function processes a series of test cases (t). For each test case, it reads an integer n from input and prints the precomputed sum of digits from 1 to n based on a preprocessed list `pd`. The function does not modify the preprocessed list `pd` or any other variables outside the loop. If the input n is less than 1 or greater than 2·10^5, no action is taken for that specific test case.

