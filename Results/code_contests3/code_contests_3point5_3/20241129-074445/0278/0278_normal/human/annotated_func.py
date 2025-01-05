#State of the program right berfore the function call: n and V are positive integers, 1 ≤ n ≤ 20, 1 ≤ V ≤ 10000. ai and bi are positive integers, 1 ≤ ai ≤ 100, 0 ≤ bi ≤ 100.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads input for `n` objects with volumes, weights, and costs. It then calculates and prints the total cost of these objects, considering their weights and costs. The function does not accept any parameters explicitly, but it expects input from the user. It calculates the total cost based on the volumes, weights, and costs of the objects.

