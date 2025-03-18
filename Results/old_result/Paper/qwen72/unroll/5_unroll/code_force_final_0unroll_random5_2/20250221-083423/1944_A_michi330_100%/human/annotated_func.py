#State of the program right berfore the function call: n is an integer where 1 ≤ n ≤ 100, and k is an integer where 0 ≤ k ≤ n * (n - 1) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The values of n and k are not retained after each iteration, and t is unchanged. For each iteration, if k is greater than or equal to n - 1, the loop prints 1; otherwise, it prints n. After all iterations, t remains the same as the initial value.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads two integers `n` and `k` from the user, where `1 ≤ n ≤ 100` and `0 ≤ k ≤ n * (n - 1) / 2`. The function then prints `1` if `k` is greater than or equal to `n - 1`, otherwise it prints `n`. After processing all `t` test cases, the function completes without returning any value, and the value of `t` remains unchanged.

