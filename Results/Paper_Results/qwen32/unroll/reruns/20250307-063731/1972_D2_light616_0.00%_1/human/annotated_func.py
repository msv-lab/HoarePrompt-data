#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_1():
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n / ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: `x` is the smallest integer greater than the square root of `n`, `y` is the value from the last iteration of the inner loop, and `cnt` is the total count of valid pairs `(x, y)`.
    print(cnt)
    #This is printed: cnt (where cnt is the total count of valid pairs (x, y) determined by the loop structure and conditions in the code)
#Overall this is what the function does:The function `func_1` reads two positive integers `n` and `m` from the input, calculates and prints the total count of valid pairs `(x, y)` where `x` and `y` are positive integers, `x` is less than or equal to the square root of `n`, and the product of `(x + y) * x` is less than or equal to `n` and `(x + y) * y` is less than or equal to `m`, with the additional condition that `x` and `y` are coprime (i.e., their greatest common divisor is 1).

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: The only variable in the initial state is `t`, and it will remain the same after the loop completes because the loop does not modify `t`. All other variables (if any) that are not part of the loop head or body remain unchanged.
    #
    #Output State:
#Overall this is what the function does:The function `func_2` reads a positive integer `t` representing the number of test cases, then calls `func_1` for each test case. It does not return any value but presumably performs operations based on the test cases.

