#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of three non-negative integers a, b, and c such that 0 ≤ a, b, c ≤ 10^9, representing the number of introverts, extroverts, and universals, respectively.
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
        
    #State: Output State: The value of `n` must be greater than 0, `i` will be equal to `n-1` or `n`, `a`, `b`, and `c` will be integers entered by the user for each iteration of the loop, and `k` will be the cumulative sum of `a + (b + c) // 3 + 1` if `(b + c) % 3 != 0` for each iteration, or just `a + (b + c) // 3` if `(b + c) % 3 == 0`.
    #
    #In simpler terms, after the loop completes all its iterations, `k` will hold the total sum of `a + (b + c) // 3 + 1` or `a + (b + c) // 3` for each set of inputs provided, adjusted based on the conditions specified in the loop.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it calculates a value based on specific conditions involving these integers and prints the result. If certain conditions are met, it adjusts the calculated value accordingly. The function ultimately outputs the cumulative sum of these adjusted values for all test cases.

