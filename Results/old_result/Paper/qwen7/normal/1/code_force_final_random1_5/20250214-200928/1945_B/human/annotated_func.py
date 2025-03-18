#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of three integers a, b, m such that 1 ≤ a, b, m ≤ 10^{18}, representing the frequency of launching for the first and second installations, and the time the firework is visible in the sky, respectively.
def func():
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        mn = min(a, b) + m
        
        if m % a == 0 and m % b == 0 and a != 1 and b != 1:
            print(mn // a + mn // b + 1)
        else:
            print(mn // a + mn // b)
        
    #State: All variables `i`, `t`, `a`, `b`, `m`, and `mn` are updated according to their respective final values after the loop completes.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of three integers `a`, `b`, and `m`. For each test case, it calculates and prints the minimum number of times two fireworks, with launch frequencies `a` and `b`, need to be launched so that both fireworks are visible simultaneously for at least `m` units of time. If `a` and `b` are not both equal to 1 and `m` is divisible by both `a` and `b`, it adds one to the result. Otherwise, it simply sums the divisions.

