#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
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
        
    #State: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively; n is an input integer. The values of a, b, and c are updated based on the input provided during each iteration of the loop, and the final values of a, b, and c after the loop are the last values read from input.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, which represents the number of test cases. For each test case, it reads three non-negative integers `a`, `b`, and `c` from the input, representing the number of introverts, extroverts, and universals, respectively. The function then calculates a value `k` based on these inputs and prints it. The value of `k` is determined by the following rules: if `b % 3 != 0` and `b % 3 + c < 3`, the function prints `-1`. Otherwise, it adds `a` to the quotient of `(b + c) // 3` and, if `(b + c) % 3 != 0`, increments `k` by 1 before printing it. After processing all test cases, the final values of `a`, `b`, and `c` are the last values read from the input for the last test case.

