#State of the program right berfore the function call: The function should take two parameters, `n` and `k`, where `n` is the number of islands (1 ≤ n ≤ 100) and `k` is the number of bridges that can be destroyed (0 ≤ k ≤ n(n - 1)/2).
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The values of `n` and `k` will be the last values read from the input in the final iteration of the loop. The value of `t` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` is the number of islands and `k` is the number of bridges that can be destroyed. The function then prints either `1` if `k` is greater than or equal to `n - 1`, or `n - 1` otherwise. The function does not return any values. After the function concludes, the values of `n` and `k` will be the last values read from the input in the final iteration of the loop, and the value of `t` remains unchanged.

