#State of the program right berfore the function call: l, r, x, and y are integers such that 1 <= l <= r <= 10^9 and 1 <= x <= y <= 10^9.
def func_1(l, r, x, y):
    if (y % x != 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: l, r, x, and y are integers such that 1 <= l <= r <= 10^9 and 1 <= x <= y <= 10^9, and y is divisible by x
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
        
    #State of the program after the  for loop has been executed: `l`, `r`, `x`, and `y` are integers such that `1 <= l <= r <= 10^9` and `1 <= x <= y <= 10^9`, `y` is divisible by `x`, `z = y / x`, and `count` is the number of pairs `(a, b)` where `a = i * x`, `b = z // i * x`, `l <= a <= r`, `l <= b <= r`, `math.gcd(a, b) == x`, and `a * b // math.gcd(a, b) == y`, with each pair contributing 1 to `count` if `a == b` and 2 if `a!= b`.
    return count
    #The program returns the total count of pairs (a, b) where a and b are within the range [l, r], a = i * x, b = z // i * x, math.gcd(a, b) == x, and a * b // math.gcd(a, b) == y, with each pair contributing 1 to count if a == b and 2 if a!= b
#Overall this is what the function does:The function accepts integers `l`, `r`, `x`, and `y` and returns 0 if `y` is not divisible by `x`, or the total count of pairs `(a, b)` within the range `[l, r]` where `a = i * x`, `b = z // i * x` (where `z = y // x`), `math.gcd(a, b) == x`, and `a * b // math.gcd(a, b) == y`, with each pair contributing 1 to the count if `a == b` and 2 if `a!= b`.

