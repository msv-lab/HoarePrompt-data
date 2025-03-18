#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9.
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
        
    #State: `a`, `b`, and `c` are assigned the values of three input integers for each iteration, `n` remains unchanged, and `i` is `n-1`. If `b % 3 != 0` and `c < 3` and `(b + c) % 3 != 0` for any iteration, `k` remains 0 for that iteration. Otherwise, `k` is updated to `k + a + (b + c) // 3` for each iteration, and if `(b + c) % 3 != 0` for any iteration, `k` is further incremented by 1 for that iteration.
#Overall this is what the function does:The function reads an integer `n` from the user, indicating the number of test cases. For each test case, it reads three non-negative integers `a`, `b`, and `c` (where 0 <= a, b, c <= 10^9). It then calculates a value `k` based on the inputs and prints it. If `b` is not divisible by 3 and `c` is less than 3, and the sum of `b` and `c` is not divisible by 3, the function prints -1. Otherwise, it calculates `k` as `a + (b + c) // 3` and increments `k` by 1 if the sum of `b` and `c` is not divisible by 3. The function does not return any value. After the function concludes, `n` remains unchanged, and `a`, `b`, and `c` are the last values read from the input for the final iteration.

