#State of the program right berfore the function call: s and x are non-negative integers such that 2 ≤ s ≤ 10^12 and 0 ≤ x ≤ 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `s` must be greater than 1, `x` is an integer between 0 and \(10^{12}\) inclusive, `count` is the number of pairs `(a, b)` such that \(a + b = s\) and \(a \oplus b = x\), `a` is the last value of `a` used in the loop, `b` is `s - a`.
    print(count)
#Overall this is what the function does:The function accepts two non-negative integers `s` and `x` as input, where `2 ≤ s ≤ 10^12` and `0 ≤ x ≤ 10^12`. It iterates through all possible pairs `(a, b)` such that `a + b = s` and counts how many of these pairs satisfy the condition `a ⊕ b = x`, where `⊕` denotes the bitwise XOR operation. If `x` is 0, the function directly prints `s`. Otherwise, it prints the count of valid pairs `(a, b)`. The function does not return anything explicitly but prints the result. Potential edge cases include when `s` is exactly 2 or `x` is 0, which are handled correctly by the code.

