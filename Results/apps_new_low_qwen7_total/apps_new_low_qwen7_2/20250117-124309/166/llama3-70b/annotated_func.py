#State of the program right berfore the function call: b, d, and s are non-negative integers such that 0 ≤ b, d, s ≤ 10^18 and b + d + s ≥ 1.
def func():
    b, d, s = map(int, input().split())

print(max(0, b - d, b - s, d - s))
#Overall this is what the function does:The function reads three non-negative integers \(b\), \(d\), and \(s\) from standard input, ensuring \(0 \leq b, d, s \leq 10^{18}\) and \(b + d + s \geq 1\). It then computes the maximum value among \(b - d\), \(b - s\), and \(d - s\), and outputs this value. The function does not return any value but prints the result directly to standard output. Potential edge cases include when one or more of the values are at their boundary conditions (0 or \(10^{18}\)). If \(b + d + s < 1\), the program will raise an error due to the initial condition check being missing.

