#State of the program right berfore the function call: The function should accept two parameters, n and k, where n is an integer representing the number of islands (1 ≤ n ≤ 100), and k is an integer representing the maximum number of bridges that Dominater can destroy (0 ≤ k ≤ n(n - 1)/2). The function should also handle multiple test cases, where the number of test cases t is an integer (1 ≤ t ≤ 10^3).
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The loop will execute `t` times, and for each iteration, it will read `n` and `k` from the input. If `k` is greater than or equal to `n - 1`, it will print `1`. Otherwise, it will print `n`. After all iterations, the value of `i` will be `t`. The values of `n`, `k`, and `t` will remain unchanged as they are input values and not modified within the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` is the number of islands and `k` is the maximum number of bridges that can be destroyed. If `k` is greater than or equal to `n - 1`, it prints `1`. Otherwise, it prints `n`. After processing all test cases, the function concludes without returning any value. The values of `t`, `n`, and `k` are not modified within the function.

