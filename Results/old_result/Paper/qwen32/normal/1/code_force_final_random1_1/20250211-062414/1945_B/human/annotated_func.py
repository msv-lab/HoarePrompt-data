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
        
    #State: The loop has executed `t` times, processing each set of integers `a`, `b`, and `m` as described. For each iteration, `mn` is calculated as `min(a, b) + m`. The program prints `mn // a + mn // b + 1` if `m` is divisible by both `a` and `b`, and neither `a` nor `b` is equal to 1; otherwise, it prints `mn // a + mn // b`.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `a`, `b`, and `m`. For each test case, it calculates a value based on these integers and prints the result. Specifically, it computes `mn` as the minimum of `a` and `b` plus `m`, and then prints either `mn // a + mn // b + 1` if `m` is divisible by both `a` and `b` and neither `a` nor `b` is 1, or `mn // a + mn // b` otherwise.

