#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers where 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: `t` is an integer input by the user where \(1 \leq t \leq 10^4\), `i` is `t`, and for each test case, `a`, `b`, and `m` are integers derived from the user's input, and `mn` is the minimum of `a` and `b` plus `m`. For each iteration, if `m` is divisible by both `a` and `b`, and neither `a` nor `b` is equal to 1, then the conditions for divisibility and non-unity of `a` and `b` are met. Otherwise, either `m` is not divisible by `a`, or `m` is not divisible by `b`, or `a` is 1, or `b` is 1.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`. It calculates the minimum of `a` and `b`, adds `m` to this minimum, and then checks if `m` is divisible by both `a` and `b` and neither `a` nor `b` is 1. If these conditions are met, it prints a specific calculation involving these values; otherwise, it prints a slightly different calculation. After processing all test cases, the function completes without returning any value.

