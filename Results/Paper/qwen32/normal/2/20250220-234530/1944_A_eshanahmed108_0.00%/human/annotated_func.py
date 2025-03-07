#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³. Each of the next t lines contains two integers n and k where 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: a sequence of t numbers, where each number is either n or 1, depending on whether the condition n - k <= 1 is true or false for each respective pair of n and k read from the input.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two integers `n` and `k`. For each test case, it prints `n` if `n - k` is less than or equal to 1; otherwise, it prints `1`.

