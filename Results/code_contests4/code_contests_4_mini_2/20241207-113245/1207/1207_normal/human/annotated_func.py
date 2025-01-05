#State of the program right berfore the function call: n is a prime integer such that 5 ≤ n < 10^9, and r is an integer such that 1 ≤ r ≤ 10^9.
def func():
    n, r = map(int, raw_input().split())
    pi = 3.141592653589793
    ans = float(n * r * r * math.sin(pi / (2 * n)) * math.sin(pi / n) / math.
    sin(3 * pi / (2 * n)))
    print(ans)
#Overall this is what the function does:The function accepts two integers `n` (a prime integer such that 5 ≤ n < 10^9) and `r` (an integer such that 1 ≤ r ≤ 10^9) as input from the user, and it computes a mathematical expression involving `n` and `r`. The result of this computation is printed to the console. However, the function does not handle any exceptions or edge cases that may arise from invalid inputs or mathematical errors, such as division by zero or invalid input types.

