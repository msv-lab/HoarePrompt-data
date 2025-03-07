#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5.
def func():
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: Output State: `t` is an input integer, `N` is 400001, `n` remains an integer such that 1 ≤ n ≤ 2⋅10^5, `pd` is a list of 400001 elements, each initialized to 0, and after executing the loop, each element `pd[i]` (for 1 ≤ i < N) is the sum of all digits of all numbers from 1 to i.
    #
    #This means that each `pd[i]` will contain the total sum of the digits of all numbers from 1 up to and including `i`. For example, `pd[3]` would be the sum of the digits of 1, 2, and 3 (which is 6), and `pd[10]` would be the sum of the digits of 1 through 10 (which is 46).
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: Output State: After executing the loop for `t` iterations, the variable `n` will be updated to the value read from input in each iteration, and `pd[n]` will be printed. The list `pd` will remain unchanged, with each element `pd[i]` (for 1 ≤ i < N) still representing the sum of all digits of all numbers from 1 to i.
#Overall this is what the function does:The function processes a series of test cases defined by the input integer `t`. For each test case, it reads an integer `n` and prints the sum of the digits of all numbers from 1 to `n`. The function initializes a list `pd` of size 400001, where each element `pd[i]` represents the sum of the digits of all numbers from 1 to `i`. After processing all test cases, the function does not return any value but prints the required sums for each `n`.

