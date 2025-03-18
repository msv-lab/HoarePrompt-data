#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are positive integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
def func():
    for q in range(int(input())):
        x, n = list(map(int, input().split(' ')))
        
        ans = 1
        
        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                if x - n * i >= 0 and (x - n * i) % i == 0:
                    ans = max(ans, i)
                if x - n * (x // i) >= 0 and x // i > 0 and (x - n * (x // i)) % (x //
                    i) == 0:
                    ans = max(ans, x // i)
        
        print(ans)
        
    #State: Output State: After the loop executes all iterations, `q` will be equal to `t - 1`, `x` will retain its original value, `ans` will be the maximum value found during all iterations of the loop that satisfy the given conditions, and `i` will be the largest integer less than or equal to the square root of `x`.
    #
    #This means that for each test case (`q`), the loop processes the values of `x` and `n` to find the maximum `i` that meets the specified conditions. After processing all `t` test cases, `q` will have been incremented `t - 1` times, making it `t - 1`. The value of `x` remains unchanged as it is only read at the start of each iteration. The variable `ans` holds the highest valid `i` found across all iterations, and `i` itself will be the largest integer less than or equal to the square root of `x` since it is the upper limit of the loop range.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers \(x\) and \(n\). For each test case, it finds the maximum integer \(i\) such that \(x - n \cdot i \geq 0\) and both \(x - n \cdot i\) and \(i\) are divisible by \(i\). The function outputs the maximum \(i\) found for each test case. After processing all test cases, it prints the results for each one.

