#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, m such that 1 ≤ a, b, m ≤ 10^{18}.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: Output State: The output state will consist of a series of integers printed as a result of the loop's execution. For each iteration `i` from `0` to `t-1`, the program reads three integers `a`, `b`, and `m` from input, calculates `mn` as `min(a, b) + m`, and then checks if `m` is divisible by both `a` and `b` without either being `1`. If the condition is met, it prints `mn // a + mn // b + 1`; otherwise, it prints `mn // a + mn // b`. This process repeats for each of the `t` iterations, and the final output state is the sequence of these printed integers.
#Overall this is what the function does:The function processes up to 10,000 test cases, each consisting of three integers \(a\), \(b\), and \(m\) (where \(1 \leq a, b, m \leq 10^{18}\)). For each test case, it calculates a value \(mn\) as the minimum of \(a\) and \(b\) plus \(m\). It then checks if \(m\) is divisible by both \(a\) and \(b\) without either being 1. If the condition is met, it prints \(mn // a + mn // b + 1\); otherwise, it prints \(mn // a + mn // b\). The function outputs a sequence of integers, one for each test case.

