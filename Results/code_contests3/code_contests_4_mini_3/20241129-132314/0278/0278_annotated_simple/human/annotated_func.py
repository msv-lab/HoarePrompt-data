#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 20, V is a positive integer such that 1 ≤ V ≤ 10000, a is a list of n positive integers where each element ai satisfies 1 ≤ ai ≤ 100, and b is a list of n non-negative integers where each element bi satisfies 0 ≤ bi ≤ 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts two integers `n` and `V`, and two lists `a` and `b` of length `n`. It computes a result based on the minimum value derived from the ratios of corresponding elements in lists `b` and `a`, multiplied by elements in list `a`, while taking into account the constraint of `V`. The function returns the computed minimum value, which is not explicitly stated in the annotations. However, it does not handle cases where `a` contains zeros, which could lead to division by zero errors.

