#State of the program right berfore the function call: l, r, x, and y are integers such that 1 ≤ l ≤ r ≤ 10^9 and 1 ≤ x ≤ y ≤ 10^9.
def func_1(l, r, x, y):
    if (y % x != 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *l, r, x, and y are integers such that 1 ≤ l ≤ r ≤ 10^9 and 1 ≤ x ≤ y ≤ 10^9. The value of y is a multiple of x.
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
        
    #State of the program after the  for loop has been executed: `count` is the total number of valid pairs `(a, b)` found based on the conditions; `l` and `r` remain unchanged; `x` and `y` remain unchanged; `z` remains equal to `y // x` and is at least 1.
    return count
    #The program returns the total number of valid pairs (a, b) found based on the conditions
#Overall this is what the function does:The function accepts four integer parameters `l`, `r`, `x`, and `y`. It first checks if `y` is a multiple of `x`; if not, it returns 0. If `y` is a multiple of `x`, it calculates pairs of integers `(a, b)` such that both are within the range `[l, r]`, their greatest common divisor is `x`, and their product equals `y`. It counts valid pairs, returning the count, which may include duplicates if `a` is equal to `b`. The function effectively counts valid pairs based on specific divisibility and range conditions.

