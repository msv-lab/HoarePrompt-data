#State of the program right berfore the function call: Each test case consists of three integers a, b, and m (1 ≤ a, b, m ≤ 10^18) where a and b represent the frequency of launching fireworks for the first and second installation respectively, and m represents the duration for which each firework is visible in the sky. There are t (1 ≤ t ≤ 10^4) such test cases.
def func():
    t = int(input())
    for _ in range(t):
        a, b, m = map(int, input().split())
        
        A = int(m / a) + 1
        
        B = int(m / b) + 1
        
        print(A + B)
        
    #State: `t` is 0; the loop has finished executing for all test cases; no further input values are read; the final outputs for all test cases have been printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `a`, `b`, and `m`. For each test case, it calculates and prints the sum of the number of times fireworks can be launched within the duration `m` for two different frequencies `a` and `b`.

