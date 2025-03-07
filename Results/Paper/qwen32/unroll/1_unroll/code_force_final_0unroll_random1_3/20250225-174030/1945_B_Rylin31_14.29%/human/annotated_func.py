#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. Each of the following t lines contains three integers a, b, and m such that 1 <= a, b, m <= 10^18.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: `t` remains unchanged, `a`, `b`, and `m` are the values from the last iteration's input.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `a`, `b`, and `m`. For each test case, it calculates and prints a result based on the values of `a`, `b`, and `m`. Specifically, it computes a value `mn` as the minimum of `a` and `b` plus `m`, and then prints the sum of the integer divisions of `mn` by `a` and `mn` by `b`, adding 1 to the result if `m` is divisible by both `a` and `b` and neither `a` nor `b` is 1.

