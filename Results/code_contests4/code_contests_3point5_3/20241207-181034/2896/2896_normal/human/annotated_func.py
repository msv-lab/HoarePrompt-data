#State of the program right berfore the function call: p1, p2, p3, p4, a, b are integers such that 1 ≤ p1, p2, p3, p4 ≤ 1000 and 0 ≤ a ≤ b ≤ 31415.
def func():
    p1, p2, p3, p4, a, b = map(int, raw_input().split())
#Overall this is what the function does:The function `func` reads input values for p1, p2, p3, p4, a, and b. It then calculates the sum of p1, p2, p3, and p4, raises this sum to the power of a, and returns the remainder when divided by b. The function does not accept any parameters explicitly.

