#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
def func_1():
    x = 1
    cnt = 0
    n, m = map(int, input().split())
    while x * x <= n:
        y = 1
        
        while (x + y) * x <= n and (x + y) * y <= m:
            if math.gcd(x, y) == 1:
                cnt += min(n // ((x + y) * x), m // ((x + y) * y))
            y += 1
        
        x += 1
        
    #State: `x` is the smallest integer greater than the square root of `n`, `y` is the last value it took in the inner loop before termination, `cnt` is the total count of valid pairs `(x, y)` satisfying the conditions, and `n` and `m` remain unchanged.
    print(cnt)
    #This is printed: cnt (where cnt is the total count of valid pairs (x, y) satisfying the conditions)
#Overall this is what the function does:The function reads two positive integers `n` and `m` from the input, then calculates and prints the total count of valid pairs `(x, y)` where `x` and `y` are positive integers, `x` is less than or equal to the square root of `n`, and the product of `(x + y) * x` is less than or equal to `n` and `(x + y) * y` is less than or equal to `m`. Additionally, `x` and `y` must be coprime (i.e., their greatest common divisor is 1).

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: t is the original number of test cases.
#Overall this is what the function does:The function `func_2` reads a positive integer `t` representing the number of test cases, then executes `func_1` for each of these test cases. It does not accept any parameters and does not return any value explicitly.

