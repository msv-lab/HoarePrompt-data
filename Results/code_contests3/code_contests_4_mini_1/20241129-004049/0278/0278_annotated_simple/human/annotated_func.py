#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 20, V is an integer such that 1 ≤ V ≤ 10000, ai is a list of n integers where each ai satisfies 1 ≤ ai ≤ 100, and bi is a list of n integers where each bi satisfies 0 ≤ bi ≤ 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 20) and an integer `V` (1 ≤ V ≤ 10000), and two lists `a` and `b` of length `n`, where each element of `a` is between 1 and 100, and each element of `b` is between 0 and 100. It calculates a minimum value based on the elements of these lists and outputs that minimum value, constrained by `V`. The exact nature of the calculation involves reducing the lists using a combination of minimum value logic and the elements from the lists but is not clearly specified in the annotations.

