#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 20, V is an integer such that 1 ≤ V ≤ 10000, a is a list of n integers where each element ai satisfies 1 ≤ ai ≤ 100, and b is a list of n integers where each element bi satisfies 0 ≤ bi ≤ 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts integer parameters `n` and `V`, and two lists of integers `a` and `b`. It computes a minimum value based on ratios of elements in `b` and `a`, but it does not handle potential division by zero errors and prints the result instead of returning it.

