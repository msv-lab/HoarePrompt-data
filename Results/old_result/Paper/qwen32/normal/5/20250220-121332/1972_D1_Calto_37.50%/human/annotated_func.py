#State of the program right berfore the function call: a and b are positive integers.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: The loop will terminate when `b` becomes zero. At this point, `a` will be the GCD of the original values of `a` and `b`.
    #
    #In natural language, this means:
    #Output State:
    return a
    #The program returns `a`, which is the GCD of the original values of `a` and `b`.
#Overall this is what the function does:The function accepts two positive integers and returns their greatest common divisor (GCD).

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n <= 2 * 10^6 and 1 <= m <= 2 * 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: `cnt` is `n + sum((n - i*(i-1)) // (i*i) for i in range(2, m)) + (m - 2)`
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: `cnt` is `n + sum((n - i*(i-1)) // (i*i) for i in range(2, m)) + (m - 2)`, and `cnt` is not equal to 0
    return cnt
    #The program returns cnt, which is calculated as `n + sum((n - i*(i-1)) // (i*i) for i in range(2, m)) + (m - 2)` and is not equal to 0.
#Overall this is what the function does:The function `func_2` takes two positive integer parameters `n` and `m` (both between 1 and 2 * 10^6). It calculates a value `cnt` based on a specific formula involving `n` and `m`. If `cnt` is 0, the function returns 1. Otherwise, it returns the calculated value of `cnt`.

