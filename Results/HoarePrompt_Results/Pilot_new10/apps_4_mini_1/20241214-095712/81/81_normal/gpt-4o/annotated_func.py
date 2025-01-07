#State of the program right berfore the function call: l, r, x, and y are integers such that 1 ≤ l ≤ r ≤ 10^9 and 1 ≤ x ≤ y ≤ 10^9.
def func_1(l, r, x, y):
    if (y % x != 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`l`, `r`, `x`, and `y` are integers such that 1 ≤ l ≤ r ≤ 10^9 and 1 ≤ x ≤ y ≤ 10^9. `y` is divisible by `x` (y % x = 0)
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
        
    #State of the program after the  for loop has been executed: `l` and `r` are integers such that 1 ≤ `l` ≤ `r`, `x` is an integer such that 1 ≤ `x`, `y` is an integer such that `x` ≤ `y`, `z` is equal to `y // x` which is a positive integer, `count` is the count of valid pairs `(a, b)` that meet the specified conditions, and `i` will iterate from 1 up to `int(math.sqrt(z))`. If the loop does not execute at all (for example, if `z` is less than 1), then `count` remains 0.
    return count
    #The program returns the count of valid pairs `(a, b)` that meet the specified conditions, where the loop iterates from 1 up to `int(math.sqrt(z))` if `z` is greater than or equal to 1. If `z` is less than 1, count remains 0.
#Overall this is what the function does:The function accepts four integer parameters `l`, `r`, `x`, and `y`, and returns 0 if `y` is not divisible by `x`. If `y` is divisible by `x`, it computes the variable `z` as `y // x`, then counts the valid pairs `(a, b)` where both `a` and `b` are multiples of `x`, fall within the range `[l, r]`, satisfy the condition that their GCD is equal to `x`, and their product equals `y`. The function returns the total count of such valid pairs, including cases where `a` equals `b`.

