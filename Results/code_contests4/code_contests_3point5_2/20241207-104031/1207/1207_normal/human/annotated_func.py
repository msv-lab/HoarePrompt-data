#State of the program right berfore the function call: n is a prime number greater than or equal to 5, and r is a positive integer greater than or equal to 1.**
def func():
    n, r = map(int, raw_input().split())
    pi = 3.141592653589793
    ans = float(n * r * r * math.sin(pi / (2 * n)) * math.sin(pi / n) / math.
    sin(3 * pi / (2 * n)))
    print(ans)
#Overall this is what the function does:The function `func` reads two inputs `n` and `r`, calculates the value of n^r - r^n using a mathematical formula, and prints the result. The constraints are that `n` must be a prime number greater than or equal to 5, and `r` must be a positive integer greater than or equal to 1.

