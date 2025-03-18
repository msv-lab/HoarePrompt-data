#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, a, b, and c are integers such that 0 <= a, b, c <= 10^9.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, and for each of the t test cases, `a`, `b`, and `c` are integers such that 0 <= a, b, c <= 10^9; `n` is an input integer. The loop has printed the result for each of the n test cases.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c`. It then calculates and prints a value `k` based on the conditions involving `b` and `c`. Specifically, if `b` modulo 3 is not zero and `b + c` is less than 3, it prints `-1`. Otherwise, it calculates `k` as `a` plus the integer division of `b + c` by 3, and if `b + c` modulo 3 is not zero, it increments `k` by 1. Finally, it prints the value of `k` for each test case.

