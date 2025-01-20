#State of the program right berfore the function call: b, d, and s are non-negative integers such that 0 ≤ b, d, s ≤ 10^18 and b + d + s ≥ 1.
def func():
    b, d, s = map(int, input().split())

print(max(0, b - d, b - s, d - s))
#Overall this is what the function does:The function reads three non-negative integers \(b\), \(d\), and \(s\) from standard input, ensuring they satisfy the conditions \(0 \leq b, d, s \leq 10^{18}\) and \(b + d + s \geq 1\). It then returns the maximum value among \(b - d\), \(b - s\), and \(d - s\). If any of these differences result in a negative number, it is treated as zero. Notably, the function does not modify any of the input values; it only computes and returns the maximum difference.

