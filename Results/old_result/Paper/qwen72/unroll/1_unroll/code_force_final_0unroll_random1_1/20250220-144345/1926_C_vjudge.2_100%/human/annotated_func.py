#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and n is an integer such that 1 <= n <= 2 * 10^5 for each test case.
def func():
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: `pd` is a list of length 200001 where each element `pd[i]` (for 1 <= i < 200001) is the sum of all the digits of the integers from 1 to i, inclusive, and the cumulative sum of the previous elements in the list.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: The list `pd` remains unchanged, and the loop prints the value of `pd[n]` for each iteration based on the input `n`.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, which represents the number of test cases. For each test case, it reads another integer `n` from user input. The function precomputes a list `pd` of length 200001, where each element `pd[i]` (for 1 <= i < 200001) is the sum of all the digits of the integers from 1 to i, inclusive, plus the cumulative sum of the previous elements in the list. After precomputation, the function prints the value of `pd[n]` for each test case. The list `pd` remains unchanged after the function concludes.

