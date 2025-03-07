#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the following t lines contains a single integer n (1 ≤ n ≤ 2 · 10^5) representing the largest number Vladislav writes on the board for that test case.
def func():
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: `t` is an integer representing the number of test cases (1 ≤ t ≤ 10^4); `N` is 200001; `pd` is a list where `pd[i]` is the cumulative sum of all previous `pd` values plus the sum of the digits of each number from 1 to `i`.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: `t` is an integer representing the number of test cases (1 ≤ t ≤ 10^4); `N` is 200001; `pd` is a list where `pd[i]` is the cumulative sum of all previous `pd` values plus the sum of the digits of each number from 1 to `i`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and outputs the cumulative sum of the digit sums of all numbers from 1 to `n`.

