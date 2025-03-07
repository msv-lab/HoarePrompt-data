#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9, representing the number of introverts, extroverts, and universals, respectively.
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
        
    #State: After the loop executes all `n` iterations, `a`, `b`, and `c` will be assigned the values from the input for each iteration, and `k` will be updated based on the conditions specified in the loop for each set of values. The loop will have executed `n` times, and `i` will be `n-1`. If `(b % 3 != 0 and c < 3) and (b + c) % 3 != 0` is true for any iteration, `-1` will be printed for that iteration. Otherwise, `k` will be updated to `k + a + (b + c) // 3`, and if `(b + c) % 3 != 0`, `k` will be further increased by 1 for that iteration. The final value of `k` will be the sum of all the updates made during the `n` iterations.
#Overall this is what the function does:The function `func` reads an integer `n` from the input, indicating the number of test cases. For each of the `n` test cases, it reads three non-negative integers `a`, `b`, and `c` from the input. The function then calculates and prints a value `k` based on the following rules: If `b % 3 != 0` and `c < 3`, and `(b + c) % 3 != 0`, it prints `-1`. Otherwise, it prints `k = a + (b + c) // 3 + 1` if `(b + c) % 3 != 0`, or `k = a + (b + c) // 3` if `(b + c) % 3 == 0`. The function does not return any value. After the function concludes, the input values `a`, `b`, and `c` for each test case will have been processed and the corresponding `k` value will have been printed for each.

