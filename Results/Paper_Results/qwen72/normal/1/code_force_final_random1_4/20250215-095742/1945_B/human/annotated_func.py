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
        
    #State: `t` is 0, `i` is `t` (which is 0), and the final outputs are determined based on the conditions evaluated during each iteration of the loop. For each iteration, `a`, `b`, and `m` were input integers, and `mn` was calculated as the minimum of `a` and `b` plus `m`. If `m` was divisible by both `a` and `b`, and neither `a` nor `b` was equal to 1, then the output was `mn // a + mn // b + 1`. Otherwise, the output was `mn // a + mn // b`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `a`, `b`, and `m`. It calculates `mn` as the minimum of `a` and `b` plus `m`. If `m` is divisible by both `a` and `b`, and neither `a` nor `b` is 1, it prints `mn // a + mn // b + 1`. Otherwise, it prints `mn // a + mn // b`. After processing all test cases, the function completes, and the final state is that `t` is 0, and the outputs for each test case have been printed.

