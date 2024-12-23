#State of the program right berfore the function call: l, r, x, and y are integers such that 1 <= l <= r <= 10^9 and 1 <= x <= y <= 10^9.
def func_1(l, r, x, y):
    if (y % x != 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: l, r, x, and y are integers such that 1 <= l <= r <= 10^9 and 1 <= x <= y <= 10^9, and y is divisible by x (i.e., y % x == 0)
    z = y // x
    count = 0
    for i in range(1, int(math.sqrt(z)) + 1):
        if z % i == 0:
            a = i * x
            b = z // i * x
            if l <= a <= r and l <= b <= r and math.gcd(a, b
                ) == x and a * b // math.gcd(a, b) == y:
                if a == b:
                    count += 1
                else:
                    count += 2
        
    #State of the program after the  for loop has been executed: `l`, `r`, `x`, and `y` retain their initial values; `z` is equal to `y // x`; `i` equals the square root of `z`; `a` and `b` are the last pair of values satisfying the loop conditions or undefined if no such pair exists; and `count` is the total number of distinct pairs of numbers `(a, b)` that satisfy the conditions within the loop, accumulated over all iterations.
    return count
    #The program returns the total number of distinct pairs of numbers (a, b) that satisfy the conditions within the loop, accumulated over all iterations
#Overall this is what the function does:The function `func_1` accepts four integer parameters `l`, `r`, `x`, and `y` and returns either `0` or the total count of distinct pairs of numbers `(a, b)` that satisfy the conditions: (1) both `a` and `b` are within the range `[l, r]`, (2) the greatest common divisor (GCD) of `a` and `b` equals `x`, and (3) the product of `a` and `b` divided by their GCD equals `y`. This count includes pairs where `a` equals `b` (counted once) and pairs where `a` is not equal to `b` (counted twice). If `y` is not divisible by `x`, the function immediately returns `0`. Upon completing its execution, the function returns the calculated count, which reflects the total number of distinct pairs satisfying these conditions within the given range and mathematical constraints. The input parameters `l`, `r`, `x`, and `y` retain their initial values throughout the function's execution.

