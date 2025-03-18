#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 2 \cdot 10^5.
def func():
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: Output State: `pd` is a list of 400001 elements where each element at index `i` (1 ≤ i ≤ 400000) contains the sum of the digits of all numbers from 1 to `i`.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: pd is a list of 400001 elements where each element at index `i` (1 ≤ i ≤ 400000) contains the sum of the digits of all numbers from 1 to `i`, and for each iteration of the loop, the script reads an integer `n` from input and prints the value of `pd[n]`. The loop runs `t` times.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` (1 ≤ t ≤ 10^4) and an integer `n` (1 ≤ n ≤ 2 * 10^5). For each test case, it calculates and prints the sum of the digits of all numbers from 1 to `n`. After processing all test cases, the function concludes with no return value.

