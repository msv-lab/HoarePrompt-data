#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: t is an input integer between 1 and 10^4, and for each test case, a, b, and m are integers such that 1 <= a, b, m <= 10^18. The loop has completed all iterations, and the final values of a, b, and m are the same as their initial values for each test case. The output for each test case is either (min(a, b) + m) // a + (min(a, b) + m) // b + 1 or (min(a, b) + m) // a + (min(a, b) + m) // b, depending on the conditions specified in the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases, where 1 <= t <= 10^4. For each test case, it reads three integers `a`, `b`, and `m` from the input, where 1 <= a, b, m <= 10^18. It calculates the value `mn` as the minimum of `a` and `b` plus `m`. If `m` is divisible by both `a` and `b` and neither `a` nor `b` is 1, it prints `mn // a + mn // b + 1`. Otherwise, it prints `mn // a + mn // b`. After processing all test cases, the function completes and the final values of `a`, `b`, and `m` for each test case are the same as their initial values.

