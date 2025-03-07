#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. Each of the t test cases is described by three non-negative integers a, b, and c such that 0 <= a, b, c <= 10^9, where a represents the number of introverts, b represents the number of extroverts, and c represents the number of universals.
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
        
    #State: `i` is `n`, `a`, `b`, and `c` are the last values read from the input, and `k` is the result of the last iteration that did not print `-1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three non-negative integers representing the counts of introverts, extroverts, and universals. For each test case, it calculates and prints a result based on these counts, or prints `-1` if certain conditions are not met.

