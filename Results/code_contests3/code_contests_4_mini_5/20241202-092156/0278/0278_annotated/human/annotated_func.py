#State of the program right berfore the function call: n is an integer between 1 and 20, V is an integer between 1 and 10000, ai is a list of n integers where each integer is between 1 and 100, and bi is a list of n integers where each integer is between 0 and 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts two integers `n` (between 1 and 20) and `V` (between 1 and 10000), along with two lists of floats `a` (containing `n` integers between 1 and 100) and `b` (containing `n` integers between 0 and 100). It calculates a minimum value based on the ratios of elements from lists `b` and `a`, multiplied by the corresponding elements of `a`, capped at `V`. The function does not handle edge cases where `b` contains zeros, which could lead to division by zero errors when calculating the ratios.

