#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10³. Each of the next t lines contains two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: A series of printed values where each value is either `n` or `1` based on the condition `n - k <= 1` for each respective pair `(n, k)` read from the input.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`. It then prints `n` if `n - k` is less than or equal to 1, otherwise it prints `1`.

