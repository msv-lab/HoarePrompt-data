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
        
    #State: Output State: The value of `k` will be the sum of `a` from each iteration plus the quotient of `(b + c) // 3`, plus an additional 1 for every iteration where `(b + c) % 3 != 0`. If during any iteration the condition `(b % 3 != 0 and c < 3) and (b + c) % 3 != 0` is met, the program will print -1 and terminate without adding to `k`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three non-negative integers \(a\), \(b\), and \(c\). For each test case, it calculates a value \(k\) based on specific conditions involving \(a\), \(b\), and \(c\). If certain conditions are met, the function prints \(-1\) and terminates without further calculations. Otherwise, it prints the calculated value \(k\). The function does not return any value but outputs the results for each test case.

