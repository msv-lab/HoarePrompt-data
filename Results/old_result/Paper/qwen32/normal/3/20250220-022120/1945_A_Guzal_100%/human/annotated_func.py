#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, a, b, and c are integers such that 0 <= a, b, c <= 10^9.
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
        
    #State: the value of `k` after all `n` iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers `a`, `b`, and `c`. For each test case, it calculates and prints a value `k` based on the conditions involving `b` and `c`. If `b` modulo 3 is not zero and the sum of `b` and `c` modulo 3 is less than 3, it prints `-1`. Otherwise, it calculates `k` as `a` plus the integer division of the sum of `b` and `c` by 3, and if the sum of `b` and `c` is not divisible by 3, it increments `k` by 1. The function prints the calculated `k` for each test case.

