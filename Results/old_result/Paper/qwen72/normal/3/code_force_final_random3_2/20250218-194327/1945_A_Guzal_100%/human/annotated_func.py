#State of the program right berfore the function call: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9.
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
        
    #State: After the loop executes all the iterations, `a`, `b`, and `c` are assigned new integer values from the input for each iteration, `i` is `n-1`, and `n` remains unchanged. For each iteration, if `b % 3 != 0` and `b % 3 + c < 3`, then `-1` is printed and `k` remains 0. Otherwise, `k` is updated to `a + (b + c) // 3`, and if `(b + c) % 3 != 0`, `k` is incremented by 1. The final value of `k` after all iterations depends on the inputs and the conditions checked in each iteration.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, indicating the number of iterations to perform. For each of the `n` iterations, it reads three non-negative integers `a`, `b`, and `c` from the user. If `b % 3 != 0` and `b % 3 + c < 3`, it prints `-1`. Otherwise, it calculates a value `k` as `a + (b + c) // 3` and increments `k` by 1 if `(b + c) % 3 != 0`. It then prints the value of `k`. After all iterations, `n` remains unchanged, and the values of `a`, `b`, and `c` are not retained for subsequent iterations. The function does not return any value.

