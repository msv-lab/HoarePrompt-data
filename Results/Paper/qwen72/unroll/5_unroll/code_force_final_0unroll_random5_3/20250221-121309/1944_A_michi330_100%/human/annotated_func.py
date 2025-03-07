#State of the program right berfore the function call: The function should take two parameters, n and k, where n is an integer representing the number of islands (1 ≤ n ≤ 100) and k is an integer representing the maximum number of bridges that can be destroyed (0 ≤ k ≤ n(n-1)/2).
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The loop will print either 1 or n for each iteration based on the condition `k >= n - 1`. The values of `t`, `n`, and `k` will be unchanged after the loop completes.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` is the number of islands (1 ≤ n ≤ 100) and `k` is the maximum number of bridges that can be destroyed (0 ≤ k ≤ n(n-1)/2). The function then prints either 1 or `n` for each test case, depending on whether `k` is greater than or equal to `n - 1`. The function does not return any value. After the function concludes, the values of `t`, `n`, and `k` are unchanged.

