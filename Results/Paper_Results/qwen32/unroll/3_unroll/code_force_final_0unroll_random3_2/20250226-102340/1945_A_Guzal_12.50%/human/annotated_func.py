#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains three integers a, b, and c such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals respectively.
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
        
    #State: t lines, each being either -1 or a calculated integer k based on the input values for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers representing the number of introverts, extroverts, and universals. For each test case, it calculates and prints a value based on these integers. The printed value is either `-1` if certain conditions are not met, or the total number of individuals adjusted by the number of extroverts and universals divided by three, with an additional increment if the sum of extroverts and universals is not divisible by three.

