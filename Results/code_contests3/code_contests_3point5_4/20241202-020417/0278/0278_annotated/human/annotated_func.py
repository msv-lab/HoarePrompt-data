#State of the program right berfore the function call: **
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads input values for `n`, `V`, `a`, and `b`. It then performs a series of calculations involving the elements of `a` and `b`, and prints the result. The function does not accept any parameters, and it does not return any value.

