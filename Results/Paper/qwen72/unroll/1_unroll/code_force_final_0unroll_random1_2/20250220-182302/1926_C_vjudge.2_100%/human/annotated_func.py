#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and n is an integer such that 1 <= n <= 2 * 10^5 for each test case.
def func():
    N = int(2 * 100000.0) + 1
    t = int(input())
    pd = [(0) for _ in range(N)]
    for i in range(1, N):
        pd[i] += pd[i - 1]
        
        for j in str(i):
            pd[i] += int(j)
        
    #State: `t` remains the same as the initial input by the user, `n` remains the same as the initial input by the user, `N` is 200001, `pd` is a list where each element `pd[i]` (for 1 <= i < N) is the sum of all elements from `pd[0]` to `pd[i-1]` plus the sum of the digits of the integer `i`.
    for _ in range(t):
        n = int(input())
        
        print(pd[n])
        
    #State: `t` remains the same as the initial input by the user, `n` is the last input value provided by the user, `N` is 200001, `pd` is a list where each element `pd[i]` (for 1 <= i < N) is the sum of all elements from `pd[0]` to `pd[i-1]` plus the sum of the digits of the integer `i`.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, which represents the number of test cases. It then precomputes a list `pd` of length 200001, where each element `pd[i]` (for 1 <= i < 200001) is the sum of all previous elements in the list plus the sum of the digits of the integer `i`. For each of the `t` test cases, the function reads another integer `n` from the user and prints the value of `pd[n]`. After processing all test cases, the function does not return any value, but the list `pd` and the integer `N` (which is 200001) remain in their final computed states. The integer `t` remains the same as the initial input, and `n` is the last input value provided by the user.

