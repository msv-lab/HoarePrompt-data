#State of the program right berfore the function call: The function should take three non-negative integers a, b, and c as input, representing the number of introverts, extroverts, and universals, respectively, with the constraints 0 <= a, b, c <= 10^9.
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
        
    #State: The values of `a`, `b`, and `c` are undefined after the loop, and `n` remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, representing the number of test cases. For each test case, it reads three non-negative integers `a`, `b`, and `c` from the input, representing the number of introverts, extroverts, and universals, respectively. The function then calculates and prints a value `k` for each test case. The value `k` is determined based on the inputs `a`, `b`, and `c` and the constraints provided. If the conditions `(b % 3 != 0 and c < 3) and (b + c) % 3 != 0` are met, the function prints `-1`. Otherwise, it calculates `k` as `a + (b + c) // 3` and adds 1 if `(b + c) % 3 != 0`. After processing all test cases, the function does not return any value, and the values of `a`, `b`, and `c` are undefined, while `n` remains unchanged.

