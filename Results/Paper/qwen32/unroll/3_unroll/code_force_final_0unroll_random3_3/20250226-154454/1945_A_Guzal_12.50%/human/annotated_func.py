#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, a, b, and c are integers such that 0 <= a, b, c <= 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if (b % 3 != 0 and c < 3) and (b + c) % 3 != 0:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: `t` is unchanged, `a`, `b`, `c` are the values from the last test case, and `k` is the result of the last test case calculation.
#Overall this is what the function does:The function processes `t` test cases, each consisting of three integers `a`, `b`, and `c`. For each test case, it calculates a value `k` based on the values of `a`, `b`, and `c` and prints either `-1` or the calculated value of `k`. The function does not return any value explicitly; it outputs the result for each test case directly.

