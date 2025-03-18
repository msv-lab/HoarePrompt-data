#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
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
        
    #State: Output State: The value of `k` will be the sum of `a + (b + c) // 3` for each iteration where `(b + c) % 3 == 0` or `(b + c) % 3 != 0`. If `(b + c) % 3 != 0`, an additional 1 is added to `k`. If `(b % 3 != 0 and b % 3 + c < 3)` is true for any iteration, the program will print -1 and terminate early. Otherwise, the final value of `k` will be printed after all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers representing the number of introverts, extroverts, and universals. For each test case, it calculates a value `k` based on specific conditions involving these integers. If any test case fails a particular condition, the function prints -1 and terminates. Otherwise, it prints the calculated value `k` for each test case after processing all cases.

