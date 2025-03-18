#State of the program right berfore the function call: The function should take three non-negative integers a, b, c (0 ≤ a, b, c ≤ 10^9) as input, representing the number of introverts, extroverts, and universals, respectively.
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
        
    #State: The values of `a`, `b`, and `c` are not retained between iterations, so they will be set to the last input values provided. The value of `k` is recalculated in each iteration based on the input values of `a`, `b`, and `c`. The loop will print a value of `k` for each iteration, and the final output state will be the last printed value of `k`.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, representing the number of test cases. For each test case, it reads three non-negative integers `a`, `b`, and `c` from the input, representing the number of introverts, extroverts, and universals, respectively. The function calculates a value `k` based on these inputs and prints it. If `b % 3 != 0` and `b % 3 + c < 3`, the function prints `-1`. Otherwise, it prints `k`, which is the sum of `a` and the integer division of `(b + c)` by 3, plus 1 if `(b + c) % 3` is not zero. The values of `a`, `b`, and `c` are not retained between iterations. The function does not return any value; it only prints the calculated values for each test case.

