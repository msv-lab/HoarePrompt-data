#State of the program right berfore the function call: b, d, and s are non-negative integers such that 0 ≤ b, d, s ≤ 10^18 and b + d + s ≥ 1.
def func():
    b, d, s = map(int, input().split())

print(max(0, b - d, b - s, d - s))
#Overall this is what the function does:The function reads three non-negative integers \( b \), \( d \), and \( s \) from the standard input, each constrained to the range \( 0 \leq b, d, s \leq 10^{18} \) and \( b + d + s \geq 1 \). It then calculates and returns the maximum value among \( b - d \), \( b - s \), and \( d - s \). If any of these values are negative, the function returns 0 instead. This ensures that the returned value is always non-negative. Potential edge cases include when one or more of the inputs are zero, or when two or more inputs are equal, leading to possible zero differences.

