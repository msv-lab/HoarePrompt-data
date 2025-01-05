#State of the program right berfore the function call: n and V are positive integers, ai and bi are non-negative integers, and 1 ≤ ai ≤ 100, 0 ≤ bi ≤ 100.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads input values for `n` and `V`, then reads lists `a` and `b`. It performs a series of calculations using lambda functions and returns the minimum value based on certain conditions. The function does not accept any parameters explicitly but operates based on the input values. It calculates and prints a certain value based on the relationships between the input lists `a` and `b`.

