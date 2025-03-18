#State of the program right berfore the function call: a and b are positive integers such that \(1 \leq a \leq n\) and \(1 \leq b \leq m\). The function `func_1` calculates the greatest common divisor (gcd) of a and b.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: a is the gcd of the original a and b, and b is 0.
    return a
    #The program returns a, which is the greatest common divisor (gcd) of the original a and b, and b is 0.
#Overall this is what the function does:The function accepts two positive integers `a` and `b` as input, calculates their greatest common divisor (gcd), and returns `a` as the gcd value while setting `b` to 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6.
def func_2(n, m):
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: cnt is -1.
    return cnt
    #The program returns -1
#Overall this is what the function does:The function accepts two positive integers, n and m, both within the range of 1 to 2⋅10^6. It initializes a counter `cnt` to -1. For each integer `i` from 1 to `m`, it calculates `x` as `n - (i * i - i)` and `y` as `i * i`. Then, it updates `cnt` by adding the result of `math.ceil(x / y)` plus 1 if `x % y` equals 0. Finally, the function returns -1 regardless of the calculations performed.

