#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3, and for each test case, x is an integer such that 1 ≤ x ≤ 10^8 and n is an integer such that 1 ≤ n ≤ x.
def func():
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        ans = 1
        
        for i in range(1, int(x ** 0.5) + 1):
            if x % i == 0:
                if n <= x // i:
                    ans = max(ans, i)
                if n <= i:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 10^3\), `x` is an integer such that \(1 \leq x \leq 10^8\), `n` is an integer such that \(1 \leq n \leq x\), `ans` is the maximum value obtained during the loop iterations among `i` and `x // i` based on the conditions provided, `i` is the largest integer such that `x` is divisible by `i` and `i` is within the range of the loop, and `ans` is printed after all iterations.
#Overall this is what the function does:The function `func` reads an integer `t` which represents the number of test cases. For each test case, it reads two integers `x` and `n`. It then iterates through all integers from 1 to the square root of `x` to find the maximum value between `i` and `x // i` that satisfies certain conditions related to `n`. Finally, it prints the maximum value found. The function does not return any value; instead, it prints the result for each test case.

