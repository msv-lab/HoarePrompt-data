#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. Each of the next t lines contains two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: t is 0.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k`. For each test case, it prints `n` if `n - k` is less than or equal to 1; otherwise, it prints 1.

