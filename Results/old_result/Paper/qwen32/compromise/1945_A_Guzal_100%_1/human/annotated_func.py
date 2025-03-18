#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9.
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
        
    #State: The output state consists of `t` test cases, each producing either `-1` or a calculated value of `k` based on the input values of `a`, `b`, and `c`. The value of `t`, `n`, and any other variables not modified within the loop remain unchanged.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three non-negative integers `a`, `b`, and `c`. For each test case, it calculates and prints either `-1` if certain conditions are not met, or a computed value `k` based on the values of `a`, `b`, and `c`. The value of `k` is determined by adding `a` to the integer division of the sum of `b` and `c` by 3, and possibly adding an additional 1 if the sum of `b` and `c` is not divisible by 3.

