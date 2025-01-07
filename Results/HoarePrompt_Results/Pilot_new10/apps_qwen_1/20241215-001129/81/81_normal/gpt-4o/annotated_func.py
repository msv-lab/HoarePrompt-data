#State of the program right berfore the function call: l, r, x, and y are integers such that 1 ≤ l ≤ r ≤ 10^9 and 1 ≤ x ≤ y ≤ 10^9.
def func_1(l, r, x, y):
    if (y % x != 0) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: l, r, x, and y are integers such that 1 ≤ l ≤ r ≤ 10^9 and 1 ≤ x ≤ y ≤ 10^9, and y is divisible by x
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
        
    #State of the program after the  for loop has been executed: `count` is the number of valid pairs \((a, b)\) found where \(a = i \cdot x\), \(b = \frac{z}{i} \cdot x\), and all conditions \(l \leq a \leq r\), \(l \leq b \leq r\), \(\text{math.gcd}(a, b) == x\), and \(a \times b // \text{math.gcd}(a, b) == y\) are satisfied. If the loop does not execute, `count` is 0.
    return count
    #The program returns count which is the number of valid pairs (a, b) found where a = i * x, b = (z / i) * x, and all conditions l ≤ a ≤ r, l ≤ b ≤ r, math.gcd(a, b) == x, and a * b // math.gcd(a, b) == y are satisfied
#Overall this is what the function does:The function `func_1` accepts four integers `l`, `r`, `x`, and `y` such that `1 ≤ l ≤ r ≤ 10^9` and `1 ≤ x ≤ y ≤ 10^9`. If `y` is not divisible by `x`, the function returns 0. Otherwise, it calculates `z` as `y // x` and iterates over possible factors of `z`. For each factor `i`, it computes pairs `(a, b)` where `a = i * x` and `b = (z // i) * x`. It checks if these pairs satisfy the conditions `l ≤ a ≤ r`, `l ≤ b ≤ r`, `math.gcd(a, b) == x`, and `a * b // math.gcd(a, b) == y`. If the pairs satisfy these conditions, it increments the count. If `a` equals `b`, it counts it as one pair; otherwise, it counts it as two pairs. Finally, the function returns the total count of valid pairs. If no valid pairs are found, it returns 0.

