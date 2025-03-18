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
        
    #State: `i` is equal to `n`, `a`, `b`, and `c` are the values from the last test case, and `k` is the value calculated for the last test case.
#Overall this is what the function does:The function processes `n` test cases, each consisting of three integers `a`, `b`, and `c`. For each test case, it calculates and prints a value `k` based on the conditions involving `b` and `c`. If `b` is not divisible by 3 and `c` is less than 3, and the sum of `b` and `c` is not divisible by 3, it prints `-1`. Otherwise, it calculates `k` as `a` plus the integer division of the sum of `b` and `c` by 3, and increments `k` by 1 if the sum of `b` and `c` is not divisible by 3. The function outputs the calculated `k` for each test case.

