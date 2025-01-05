#State of the program right berfore the function call: n is a prime integer such that 5 ≤ n < 10^9, and r is an integer such that 1 ≤ r ≤ 10^9.
def func():
    n, r = map(int, raw_input().split())
    pi = 3.141592653589793
    ans = float(n * r * r * math.sin(pi / (2 * n)) * math.sin(pi / n) / math.
    sin(3 * pi / (2 * n)))
    print(ans)
#Overall this is what the function does:The function reads two integers, a prime integer `n` (where 5 ≤ n < 10^9) and an integer `r` (where 1 ≤ r ≤ 10^9), from input and calculates a mathematical expression involving these values. It then prints the result of the calculation as a floating-point number. The function does not return a value, as the output is printed directly. There are no explicit checks for invalid input or handling for edge cases in the calculation.

