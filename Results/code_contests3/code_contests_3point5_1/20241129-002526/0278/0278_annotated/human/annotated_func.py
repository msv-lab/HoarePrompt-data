#State of the program right berfore the function call: n and V are positive integers such that 1 ≤ n ≤ 20 and 1 ≤ V ≤ 10000. ai and bi are non-negative integers such that 1 ≤ ai ≤ 100 and 0 ≤ bi ≤ 100.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads input values for n, V, ai, and bi. It then calculates and prints a value based on the input values using a complex nested calculation involving min, reduce, zip, and lambda functions. The function does not accept any parameters and operates solely on the user's input.

