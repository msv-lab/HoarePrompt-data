#State of the program right berfore the function call: n and V are positive integers such that 1 <= n <= 20 and 1 <= V <= 10000. ai and bi are positive integers such that 1 <= ai <= 100 and 0 <= bi <= 100.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:Functionality: The function `func` reads input values for `n`, `V`, `a`, and `b` from the user. It then calculates a value based on the given formula and constraints. The function does not have a specific return value. However, it performs a complex calculation involving the input values and prints the result. It operates within the constraints of the positive integers `n` and `V`, where 1 <= n <= 20 and 1 <= V <= 10000, as well as the positive integers `ai` and `bi`, where 1 <= ai <= 100 and 0 <= bi <= 100. Make sure to note that the function uses reduce and lambda functions to calculate this value based on the given formula.

