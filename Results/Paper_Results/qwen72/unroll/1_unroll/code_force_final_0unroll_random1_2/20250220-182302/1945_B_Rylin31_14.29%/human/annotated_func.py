#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, a, b, and m are integers such that 1 ≤ a, b, m ≤ 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: The values of `t`, `a`, `b`, and `m` remain unchanged, but the loop has completed its execution, and the output has been printed for each test case.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `a`, `b`, and `m` from the input. It then calculates a value `mn` as the minimum of `a` and `b` plus `m`. If `m` is divisible by both `a` and `b` and neither `a` nor `b` is 1, it prints the result of `mn // a + mn // b + 1`. Otherwise, it prints `mn // a + mn // b`. After processing all test cases, the function completes and no values are returned. The state of the program remains unchanged except for the output that has been printed for each test case.

