#State of the program right berfore the function call: n is an integer in the range 1 to 20, V is an integer in the range 1 to 10000, a is a list of n integers where each integer ai is in the range 1 to 100, and b is a list of n integers where each integer bi is in the range 0 to 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts an integer `n` (1 to 20) and an integer `V` (1 to 10000), as well as two lists `a` and `b` of size `n`, where each element of `a` is an integer (1 to 100) and each element of `b` is an integer (0 to 100). It processes these inputs to compute and print the minimum value obtained from a specific calculation involving the ratios of elements in lists `b` and `a`, multiplied by elements in list `a`, constrained by `V`. The function does not handle any edge cases such as invalid input formats or values outside the specified ranges.

