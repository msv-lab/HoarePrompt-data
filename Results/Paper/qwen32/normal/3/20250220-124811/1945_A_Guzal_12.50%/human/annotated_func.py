#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains three integers a, b, and c such that 0 <= a, b, c <= 10^9, where a represents the number of introverts, b represents the number of extroverts, and c represents the number of universals.
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
        
    #State: After `n` iterations, the final value of `k` is printed. If at any iteration `(b % 3 != 0 and c < 3) and (b + c) % 3 != 0`, `-1` is printed for that iteration and `k` is not updated for that iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers representing the counts of introverts, extroverts, and universals. For each test case, it calculates and prints the total count of individuals, adjusted based on specific conditions related to the counts of extroverts and universals. If certain conditions are not met, it prints `-1` for that test case.

