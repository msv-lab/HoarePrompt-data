#State of the program right berfore the function call: x is an integer such that -10^9 ≤ x ≤ 10^9.
def func():
    n = abs(input())
    d = int(ceil((sqrt(1 + 8 * n) - 1) / 2))
    print[[0, 2, 1, 0], [1, 0, 0, 2]][n % 2][d % 4] + d
#Overall this is what the function does:The function accepts an integer input from the user, calculates a derived value based on that input, and prints the result, but does not return anything and lacks error handling for invalid input types.

