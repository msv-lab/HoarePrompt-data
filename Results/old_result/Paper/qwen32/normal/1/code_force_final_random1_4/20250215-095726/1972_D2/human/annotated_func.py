#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
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
        
    #State: n is 5, m is 20, x is 3, y is 5, and cnt is 2.5.
    print(cnt)
    #This is printed: 2.5
#Overall this is what the function does:The function calculates and prints a count based on the number of pairs `(x, y)` where `x` and `y` are positive integers, `gcd(x, y) == 1`, and the product `(x + y) * x` does not exceed `n` and `(x + y) * y` does not exceed `m`. The result is a floating-point number representing the sum of minimum possible values derived from these conditions.

#State of the program right berfore the function call: t is a positive integer representing the number of test cases, where 1 <= t <= 10^4.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: `t` is the integer value provided by the user input, where 1 <= `t` <= 10^4.
#Overall this is what the function does:The function `func_2` reads a positive integer `t` from the input, representing the number of test cases. It then processes each of these `t` test cases by calling `func_1()` for each one. The function does not return any value explicitly, but it implicitly returns the results of processing the test cases through the operations performed within `func_1()`.

