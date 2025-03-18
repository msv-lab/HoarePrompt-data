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
        
    #State of the program after the  for loop has been executed: `l` is an integer such that \(1 \leq l \leq r \leq 10^9\); `r` is an integer such that \(1 \leq l \leq r \leq 10^9\); `x` is an integer such that \(1 \leq x \leq y \leq 10^9\) and \(y\) is divisible by \(x\); `y` is an integer such that \(1 \leq x \leq y \leq 10^9\) and \(y\) is divisible by \(x\); `z` is \(y // x\); `count` is the total number of valid pairs \((a, b)\) found during the loop execution, where \(a\) and \(b\) are within the range \([l, r]\), their GCD is \(x\), and their product divided by their GCD equals \(y\); `a` and `b` are the last valid pair found during the loop execution.
    return count
    #The program returns count, which is the total number of valid pairs (a, b) found during the loop execution, where a and b are within the range [l, r], their GCD is x, and their product divided by their GCD equals y
#Overall this is what the function does:The function `func_1` accepts four integers `l`, `r`, `x`, and `y` such that \(1 \leq l \leq r \leq 10^9\) and \(1 \leq x \leq y \leq 10^9\). It returns either 0 or the count of valid pairs \((a, b)\) that satisfy the following conditions:
- \(l \leq a, b \leq r\)
- \(\text{gcd}(a, b) = x\)
- \(a \times b / \text{gcd}(a, b) = y\)

