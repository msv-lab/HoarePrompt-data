#State of the program right berfore the function call: t is a positive integer representing the number of test cases, and each test case consists of three positive integers n, a, and b such that 1 ≤ n, a, b ≤ 10^9.
def func():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: t is 0, and the values of n, a, and b are undefined.
#Overall this is what the function does:The function processes `t` test cases, where `t` is the number of test cases provided as input. For each test case, it reads three positive integers `n`, `a`, and `b`. Depending on the relationship between `a`, `b`, and `n`, it calculates and prints one of three possible results. After processing all test cases, the function ends without returning any value.

