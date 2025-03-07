#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, a, and b are integers such that 1 ≤ n ≤ 100 and 1 ≤ a, b ≤ 30.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        d = c / 2
        
        if a * b < a * d:
            print(a * b)
        else:
            print(round(a * d))
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer representing the number of iterations, `i` is equal to `n`, and for each of the `n` iterations, the values of `a`, `b`, and `c` are integers read from the input, `d` is `c / 2`. The program has printed either `a * b` or `round(a * d)` for each iteration based on the condition `a * b < a * d`.
#Overall this is what the function does:The function reads an integer `n` representing the number of iterations. For each iteration, it reads three integers `a`, `b`, and `c`. It calculates `d` as half of `c` and prints either `a * b` or the rounded value of `a * d`, depending on whether `a * b` is less than `a * d`.

