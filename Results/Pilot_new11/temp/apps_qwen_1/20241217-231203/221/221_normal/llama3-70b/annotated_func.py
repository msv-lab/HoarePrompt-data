#State of the program right berfore the function call: s and x are integers such that 2 ≤ s ≤ 10^12 and 0 ≤ x ≤ 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `s` is an integer between 2 and \(10^{12}\), `x` is an integer between 0 and \(10^{12}\), `count` is the number of pairs `(a, b)` such that \(a + b = s\) and \(a \oplus b = x\), `a` is the last value of `a` used in the loop (which will be `s`), `b` is `s - a` (which will be 0), and \(a \oplus b\) is equal to `x`.
    print(count)
#Overall this is what the function does:The function accepts two integers `s` and `x` where \(2 \leq s \leq 10^{12}\) and \(0 \leq x \leq 10^{12}\). It iterates through all possible values of `a` from 1 to `s-1`, calculates `b` as `s - a`, and checks if the bitwise XOR of `a` and `b` equals `x`. It counts the number of pairs `(a, b)` that satisfy both conditions and prints the count. If no such pairs exist, the count will be 0. The function does not return anything; it only prints the count. Potential edge cases include when `s` is very large, which might cause performance issues due to the iteration over a large range.

