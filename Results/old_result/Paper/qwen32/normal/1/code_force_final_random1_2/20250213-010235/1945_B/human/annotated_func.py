#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each of the next t lines contains three integers a, b, and m such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: The loop has completed `t` iterations, and `i` is equal to `t`. The values of `a`, `b`, `m`, and `mn` are not retained as they were updated in each iteration.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints a value based on the conditions involving `a`, `b`, and `m`. Specifically, it computes a minimum value `mn` as the smaller of `a` and `b` plus `m`, and then determines the output by dividing `mn` by `a` and `b`, adding these results, and possibly adding one more if `m` is divisible by both `a` and `b` and neither `a` nor `b` is 1. After processing all test cases, the function terminates without retaining any intermediate values.

