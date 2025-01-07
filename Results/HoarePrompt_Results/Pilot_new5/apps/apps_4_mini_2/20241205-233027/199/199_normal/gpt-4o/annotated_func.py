#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^9.
def func_1(n):
    if (n < 6) :
        return 0
        #The program returns 0
    #State of the program after the if block has been executed: *`n` is a positive integer such that 1 ≤ `n` ≤ 2·10^9, and `n` is greater than or equal to 6.
    count = 0
    for a in range(1, n // 4 + 1):
        b = a
        
        rem = n - 2 * (a + b)
        
        if rem > 0 and rem % 2 == 0:
            if a != rem // 2:
                count += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (≥ 6), `count` is the total number of valid pairs, `a` is \(n // 4\), `b` is \(n // 4\), and `rem` is \(n - 4 \cdot (n // 4)\).
    return count
    #The program returns the total number of valid pairs, which is stored in the variable 'count'.
#Overall this is what the function does:The function accepts a positive integer `n` (where 1 ≤ n ≤ 2·10^9) and returns 0 if `n` is less than 6. If `n` is 6 or greater, it calculates and returns the total number of valid pairs `(a, b)` such that `2 * (a + b)` is less than `n` and `rem`, the remainder after subtracting `2 * (a + b)` from `n`, is positive and even. The valid pairs are counted based on the condition that `a` must not equal `rem // 2`.

