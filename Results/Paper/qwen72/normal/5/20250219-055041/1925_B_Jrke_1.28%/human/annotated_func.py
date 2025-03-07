#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^3, x is an integer such that 1 <= x <= 10^8, and n is an integer such that 1 <= n <= x. Each test case is represented by a pair of integers (x, n).
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        if k == 1:
            print(1)
            continue
        
        ans = 1
        
        for i in range(1 + (1 if x % 2 == 0 else 0), int(x ** 0.5) + 1, 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: `t` is an integer such that 1 <= t <= 10^3, `x` is the last integer input from the test cases, `n` is the last integer input from the test cases, `k` is the integer division of the last `x` by the last `n` (i.e., `k = x // n`), and `i` is the last value of the loop variable `i` that was used in the inner loop, which is an odd integer between 1 and the square root of the last `x` (inclusive), incremented by 2 each step. The variable `ans` holds the maximum value found in the inner loop for the last test case, which is either 1, `i`, or `x // i` if they are less than or equal to `k`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, and for each test case, it reads a pair of integers `x` and `n`. It then computes the largest divisor of `x` that is less than or equal to `k` (where `k = x // n`), and prints this value. If no such divisor exists or if `k` is 1, it prints 1. After processing all test cases, the function concludes, and the variables `t`, `x`, `n`, `k`, and `i` retain their last values from the final test case. The variable `ans` holds the maximum divisor found for the last test case, which is either 1, `i`, or `x // i` if they are less than or equal to `k`.

