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
        
    #State: a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9; n is an input integer. The values of a, b, and c are updated in each iteration based on user input, and k is recalculated in each iteration. After n iterations, the final values of a, b, and c are the ones provided in the last iteration of input, and k is the value calculated in the last iteration.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, indicating the number of test cases. For each test case, it reads three non-negative integers `a`, `b`, and `c` from the user, where 0 <= a, b, c <= 10^9. It then calculates a value `k` based on the following rules: if `(b % 3 != 0 and c < 3)` and `(b + c) % 3 != 0`, it prints `-1`. Otherwise, it calculates `k` as `a + (b + c) // 3` and increments `k` by 1 if `(b + c) % 3 != 0`. The function prints the value of `k` for each test case. After processing `n` test cases, the function ends. The final state of the program is that `a`, `b`, and `c` are the values provided in the last test case, and `k` is the value calculated in the last test case.

