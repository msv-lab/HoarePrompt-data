#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
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
        
    #State: x is the smallest integer for which x * x is greater than n, y is 1, cnt is the total count calculated based on the conditions inside the loops.
    print(cnt)
    #This is printed: cnt (where cnt is the total count calculated based on the conditions inside the loops)
#Overall this is what the function does:The function `func_1` accepts two positive integer parameters `n` and `m` and calculates a count based on certain conditions involving pairs of integers `x` and `y` where `x` and `y` are coprime. It then prints this count.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2():
    t = int(input())
    for _ in range(t):
        func_1()
        
    #State: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6; t is an input integer.
#Overall this is what the function does:The function `func_2` reads an integer `t` from the input, then calls `func_1` exactly `t` times. The parameters `n` and `m` are mentioned in the annotations but are not used within `func_2` itself. The function does not return any value explicitly, and the final state of the program after it concludes is that `func_1` has been executed `t` times.

