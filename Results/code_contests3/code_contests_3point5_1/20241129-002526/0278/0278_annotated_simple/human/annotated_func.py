#State of the program right berfore the function call: n and V are positive integers such that 1 <= n <= 20 and 1 <= V <= 10000. ai and bi are non-negative integers such that 1 <= ai, bi <= 100.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads input values for n, V, ai, and bi. It then performs calculations on the input values without explicitly stating the purpose or outcome of these calculations. The function does not accept any parameters, and the output of the function is not specified in the given information. The actual functionality based on the code provided is unclear due to the complexity of the calculations performed.

