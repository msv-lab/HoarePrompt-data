#State of the program right berfore the function call: The function should take three non-negative integers a, b, and c as input, where 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
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
        
    #State: `n` is equal to the initial value of `n`, `i` is `n - 1`, `a`, `b`, and `c` are input integers. For each iteration, if `(b % 3 != 0 and c < 3) and (b + c) % 3 != 0`, `k` remains 0. Otherwise, `k` is set to `a + (b + c) // 3`, and if `(b + c) % 3 != 0`, `k` is incremented by 1.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, representing the number of test cases. For each test case, it reads three non-negative integers `a`, `b`, and `c` (where `0 <= a, b, c <= 10^9`) from the input, representing the number of introverts, extroverts, and universals, respectively. The function then calculates and prints a value `k` for each test case. The value of `k` is determined as follows: if `(b % 3 != 0 and c < 3) and (b + c) % 3 != 0`, `k` is set to `-1`. Otherwise, `k` is set to `a + (b + c) // 3`, and if `(b + c) % 3 != 0`, `k` is incremented by 1. The function does not return any value; it only prints the calculated `k` for each test case. After the function concludes, `n` is unchanged, and `i` is `n - 1`. The values of `a`, `b`, and `c` are reset for each test case.

