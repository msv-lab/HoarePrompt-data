#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the next t lines contains three integers a, b, and c such that 0 <= a, b, c <= 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if b % 3 != 0 and b % 3 + c < 3:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: `t` is an integer such that 1 <= t <= 10^4; each of the next t lines contains three integers a, b, and c such that 0 <= a, b, c <= 10^9; `n` is an input integer; `k` is the cumulative sum of `a + (b + c) // 3` for each iteration where `b % 3 != 0` or `b % 3 + c >= 3`, incremented by 1 additional unit if `(b + c) % 3 != 0` in those iterations.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers `a`, `b`, and `c`. For each test case, it calculates and prints a result based on the values of `a`, `b`, and `c`. Specifically, it prints `-1` if `b` is not divisible by 3 and the sum of `b` and `c` is less than 3. Otherwise, it calculates a value `k` as the sum of `a` and the integer division of the sum of `b` and `c` by 3, and increments `k` by 1 if the sum of `b` and `c` is not divisible by 3, before printing `k`.

