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
        
    #State: After the loop executes all its iterations, `t` is a positive integer such that \(1 \leq t \leq 10^4\), `i` is equal to `n-1`, `n` is the number of times the loop was executed, `a`, `b`, and `c` are integers obtained from the input split by spaces for each iteration, and `k` is the sum of `a + (b + c) // 3 + 1` for each iteration where `(b + c) % 3` is not equal to 0 and `a + (b + c) // 3` otherwise.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three non-negative integers (a, b, and c) representing the number of introverts, extroverts, and universals, respectively. For each test case, it calculates a value k based on the given conditions. If the value of a is outside the range 1 to 10^4, it prints an error message. Otherwise, it computes k as the sum of a plus one-third of (b + c) rounded down, plus one if (b + c) is not divisible by 3. It then prints the computed value k for each test case.

