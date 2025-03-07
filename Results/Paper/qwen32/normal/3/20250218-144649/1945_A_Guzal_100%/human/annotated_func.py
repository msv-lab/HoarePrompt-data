#State of the program right berfore the function call: Each test case consists of three non-negative integers a, b, and c, where 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals respectively. There are t test cases, where 1 <= t <= 10^4.
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
        
    #State: the final value of `k` after all `n` iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it calculates and prints a total count based on specific conditions involving the divisibility of the sum of extroverts and universals by 3. If the conditions are not met, it prints -1.

