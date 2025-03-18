#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains a single integer n (1 ≤ n ≤ 2 · 10^5) which is the largest number Vladislav writes on the board.
def func():
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: `pd` list updated with cumulative sums of digit sums, `t` and `N` unchanged.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: `pd` list updated with cumulative sums of digit sums, `t` and `N` unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints the cumulative sum of the digit sums of all integers from 1 to `n`.

