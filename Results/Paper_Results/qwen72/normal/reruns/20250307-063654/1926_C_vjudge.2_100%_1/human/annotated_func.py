#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and n is an integer such that 1 ≤ n ≤ 2 · 10^5 for each test case.
def func():
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: `t` is an integer input by the user, 1 ≤ t ≤ 10^4, `n` is an integer such that 1 ≤ n ≤ 2 · 10^5 for each test case, `N` is 200001, `pd` is a list of 200001 integers where `pd[i]` is the cumulative sum of the digits of all integers from 1 to `i` for each `i` in the range 1 to `N-1`, and `i` is `N-1`.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: `t` is an integer input by the user, 1 ≤ t ≤ 10^4, `_` is `t-1`, `n` is an integer input by the user, `N` is 200001, `pd` is a list of 200001 integers where `pd[i]` is the cumulative sum of the digits of all integers from 1 to `i` for each `i` in the range 1 to `N-1`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, where `1 ≤ t ≤ 10^4`, and then for each of the `t` test cases, it reads another integer `n` from the user, where `1 ≤ n ≤ 2 · 10^5`. It precomputes a list `pd` of length 200001, where `pd[i]` represents the cumulative sum of the digits of all integers from 1 to `i` for each `i` in the range 1 to 200000. For each test case, it prints the value of `pd[n]`, which is the cumulative sum of the digits of all integers from 1 to `n`. After processing all test cases, the function does not return any value.

