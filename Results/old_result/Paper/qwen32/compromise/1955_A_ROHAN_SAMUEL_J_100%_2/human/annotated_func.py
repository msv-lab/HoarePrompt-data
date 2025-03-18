#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, a, and b are integers such that 1 <= n <= 100, 1 <= a <= 30, and 1 <= b <= 30.
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
        
    #State: The loop has finished executing all iterations, and the output consists of `t` lines, each line being the result of the computation for each test case based on the provided logic. The variables `n`, `a`, and `b` from the last iteration are not part of the output state.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `n`, `a`, and `b`. For each test case, it computes and prints a value based on the relationship between `n`, `a`, and `b`. Specifically, it prints the minimum cost to achieve a certain configuration, either by using `a` for each unit or using `b` for pairs, considering whether `n` is odd or even.

