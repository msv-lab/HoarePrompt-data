#State of the program right berfore the function call: n and V are positive integers such that 1 <= n <= 20 and 1 <= V <= 10000. ai and bi are non-negative integers such that 1 <= ai <= 100 and 0 <= bi <= 100.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads input values for `n`, `V`, `a`, and `b`. It then calculates a result based on a complex nested lambda function, but the purpose or meaning of this calculation is not clear from the code provided. The function does not have a specified return value. The annotations provide information about the expected input values, constraints, and data types, but the actual functionality of the function based on the code is not explicitly described.

