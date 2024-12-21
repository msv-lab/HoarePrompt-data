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
        
    #State of the program after the  for loop has been executed: `l` and `r` are integers such that `1 <= l <= r <= 10^9`, `x` and `y` are integers such that `1 <= x <= y <= 10^9` and `y` is divisible by `x`, `z` is `y // x`, and `count` is the number of pairs of divisors of `y` that meet the given conditions.
    return count
    #The program returns the number of pairs of divisors of `y` that meet the specified conditions, where `y` is divisible by `x`, and both `x` and `y` are integers between 1 and 10^9.
#Overall this is what the function does:The function `func_1` accepts four parameters: `l`, `r`, `x`, and `y`, which are integers within specified ranges (1 <= `l` <= `r` <= 10^9 and 1 <= `x` <= `y` <= 10^9). It checks if `y` is divisible by `x` and returns 0 if not. If `y` is divisible by `x`, it calculates the number of pairs of divisors of `y` that meet the conditions: both divisors are within the range `[l, r]`, their greatest common divisor is `x`, and their product is `y`. The function counts each pair of distinct divisors twice and each pair of equal divisors once. The function returns this count, which represents the number of pairs of divisors of `y` that satisfy the given conditions. The function handles all potential edge cases, including cases where `y` is not divisible by `x`, cases where there are no divisors of `y` within the range `[l, r]`, and cases where `a` equals `b`.

