#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the next t lines contains three integers a, b, and c, where 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
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
        
    #State: the accumulated value of k after all iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads three integers `a`, `b`, and `c` representing the number of introverts, extroverts, and universals, respectively. It then calculates and prints the total count of individuals based on the given conditions. If the conditions are not met, it prints `-1`.

