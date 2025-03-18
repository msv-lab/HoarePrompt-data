#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        if n % 2:
            if 2 * a < b:
                print(a * n)
            else:
                print(n // 2 * b + a)
        elif 2 * a < b:
            print(a * n)
        else:
            print(n // 2 * b)
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30. The program prints the result for each test case based on the given conditions.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `n`, `a`, and `b`. For each test case, it calculates and prints the minimum cost based on the given conditions: if `n` is odd, it compares `2 * a` with `b` to determine the cost, and if `n` is even, it similarly compares `2 * a` with `b` to decide whether to use `a * n` or `n // 2 * b` for the cost.

