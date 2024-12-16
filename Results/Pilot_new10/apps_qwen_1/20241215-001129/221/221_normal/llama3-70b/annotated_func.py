#State of the program right berfore the function call: s and x are non-negative integers such that 2 ≤ s ≤ 10^12 and 0 ≤ x ≤ 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `s` is a non-negative integer such that \(2 \leq s \leq 10^{12}\) and `s` is greater than 1, `x` is equal to its original value, `count` is the number of pairs `(a, b)` where `a` is in the range `[1, s-1]`, `b = s - a`, and `a ^ b == x`, `a` and `b` are values from the last valid pair that satisfies `a ^ b == x` (or their original values if no such pair exists), and `b` is `s - a`.
    print(count)
#Overall this is what the function does:The function accepts two non-negative integers `s` and `x` with constraints \(2 \leq s \leq 10^{12}\) and \(0 \leq x \leq 10^{12}\). It calculates and prints the number of pairs `(a, b)` such that `a` is in the range `[1, s-1]`, `b = s - a`, and `a ^ b == x`.

