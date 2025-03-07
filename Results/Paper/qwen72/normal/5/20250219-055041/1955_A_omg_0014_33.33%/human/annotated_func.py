#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, n, a, and b are integers such that 1 <= n <= 100 and 1 <= a, b <= 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is an integer such that `n` >= 1, `i` is `n - 1`, and for each iteration `a`, `b`, and `c` are integers such that 1 <= a, b, c <= 30. `d` is equal to `c / 2` for each iteration. For each iteration, if `a * b` is less than `a * d`, the condition `a * b < a * d` holds true and `a * b` is printed. Otherwise, `a * b` is greater than or equal to `a * d` and `round(a * d)` is printed.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` from the input. It then calculates `d` as half of `c`. If `a * b` is less than `a * d`, it prints `a * b`; otherwise, it prints the rounded value of `a * d`. After processing all `n` test cases, the function completes, and the final state is that `n` test cases have been processed, with the appropriate values printed for each case.

