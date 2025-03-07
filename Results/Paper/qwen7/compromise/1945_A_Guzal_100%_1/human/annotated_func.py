#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c representing the number of introverts, extroverts, and universals, respectively, such that 0 ≤ a, b, c ≤ 10^9.
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
        
    #State: Output State: The value of `t` remains unchanged, and for each iteration of the loop, the variable `k` is updated based on the input values `a`, `b`, and `c`. If the condition `b % 3 != 0 and b % 3 + c < 3` is met, the program prints `-1` and does not update `k`. Otherwise, `k` is updated by adding `a + (b + c) // 3` and then potentially adding `1` if `(b + c) % 3 != 0`. After all iterations, the final value of `k` is printed.
#Overall this is what the function does:The function processes a series of test cases, each containing three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it calculates and prints a value `k` based on specific conditions. If certain conditions are not met, it prints `-1` for that test case. The final output for each test case is the calculated value `k`.

