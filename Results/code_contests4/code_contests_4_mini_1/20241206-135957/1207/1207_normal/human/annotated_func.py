#State of the program right berfore the function call: n is a prime integer such that 5 ≤ n < 10^9, and r is an integer such that 1 ≤ r ≤ 10^9.
def func():
    n, r = map(int, raw_input().split())
    pi = 3.141592653589793
    ans = float(n * r * r * math.sin(pi / (2 * n)) * math.sin(pi / n) / math.
    sin(3 * pi / (2 * n)))
    print(ans)
#Overall this is what the function does:The function accepts two parameters, `n`, a prime integer where \(5 \leq n < 10^9\), and `r`, an integer where \(1 \leq r \leq 10^9\). It calculates a specific mathematical expression involving trigonometric functions and prints the result. Note that the function does not handle invalid inputs or any errors that may occur during the input reading or the calculations.

