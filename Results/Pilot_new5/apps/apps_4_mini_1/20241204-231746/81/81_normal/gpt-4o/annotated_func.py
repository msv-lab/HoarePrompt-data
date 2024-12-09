#State of the program right berfore the function call: l, r, x, and y are integers such that 1 ≤ l ≤ r ≤ 10^9 and 1 ≤ x ≤ y ≤ 10^9.
def func_1(l, r, x, y):
    if (y % x != 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`l`, `r`, `x`, and `y` are integers such that 1 ≤ `l` ≤ `r` ≤ 10^9 and 1 ≤ `x` ≤ `y` ≤ 10^9. The value of `y` is a multiple of `x`.
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
        
    #State of the program after the  for loop has been executed: `l` and `r` are integers such that 1 ≤ `l` ≤ `r` ≤ 10^9; `x` and `y` are integers such that 1 ≤ `x` ≤ `y` ≤ 10^9 and `y` is a multiple of `x`; `z` is equal to `y // x`; `count` is the total number of valid pairs `(a, b)` found where `a` and `b` satisfy the conditions `l ≤ a ≤ r`, `l ≤ b ≤ r`, `math.gcd(a, b) == x`, and `a * b // math.gcd(a, b) == y`. If no pairs satisfy these conditions, `count` remains 0.
    return count
    #The program returns the total number of valid pairs (a, b) found where a and b satisfy the conditions l ≤ a ≤ r, l ≤ b ≤ r, math.gcd(a, b) == x, and a * b // math.gcd(a, b) == y. If no pairs satisfy these conditions, count remains 0.
#Overall this is what the function does:The function accepts four integer parameters `l`, `r`, `x`, and `y`, and returns 0 if `y` is not a multiple of `x`. If `y` is a multiple of `x`, it calculates and returns the total number of valid pairs `(a, b)` such that both `a` and `b` are within the range `[l, r]`, `math.gcd(a, b)` equals `x`, and `a * b / math.gcd(a, b)` equals `y`. If no valid pairs are found that satisfy these conditions, the function returns 0.

