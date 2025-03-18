#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n is an integer such that 1 <= n <= 2 * 10^5.
def func():
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: `pd` is a list where `pd[i]` is the cumulative sum of all the previous `pd` values plus the sum of the digits of each number from 1 to `i`, for `i` from 1 to 200000, and `pd[0]` remains 0.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: `pd` is a list where `pd[i]` is the cumulative sum of all the previous `pd` values plus the sum of the digits of each number from 1 to `i`, for `i` from 1 to 200000, and `pd[0]` remains 0.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n`. For each test case, it computes and prints a cumulative sum that includes the sum of the digits of all numbers from 1 to `n`.

