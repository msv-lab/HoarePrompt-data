#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, x and n are positive integers such that 1 ≤ x ≤ 10^8 and 1 ≤ n ≤ x.
def func_1():
    x, n = list(map(int, input().split()))
    ans = 0
    for i in range(1, isqrt(x) + 1):
        if x % i == 0:
            if n <= x // i:
                ans = max(ans, i)
            if n <= i:
                ans = max(ans, x // i)
        
    #State: Output State: `t` is a positive integer such that 1 ≤ t ≤ 10^3, `x` is an input integer such that 1 ≤ x ≤ 10^8, `n` is an input integer such that 1 ≤ n ≤ x, `ans` is the maximum value between any divisor `i` of `x` and `x//i` where both `i` and `x//i` are greater than or equal to `n`.
    print(ans)
    #This is printed: ans (where ans is the maximum value between any divisor i of x and x//i where both i and x//i are greater than or equal to n)
#Overall this is what the function does:The function reads two integers \(x\) and \(n\) from input, where \(1 \leq x \leq 10^8\) and \(1 \leq n \leq x\). It then calculates and prints the maximum value between any divisor \(i\) of \(x\) and \(x//i\) where both \(i\) and \(x//i\) are greater than or equal to \(n\). The function processes up to \(10^3\) test cases.

