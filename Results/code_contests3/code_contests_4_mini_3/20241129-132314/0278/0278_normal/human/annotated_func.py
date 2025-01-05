#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 20, V is an integer such that 1 ≤ V ≤ 10000, a is a list of n integers where each integer ai satisfies 1 ≤ ai ≤ 100, and b is a list of n integers where each integer bi satisfies 0 ≤ bi ≤ 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts two integers `n` (in the range 1 to 20) and `V` (in the range 1 to 10000), along with two lists `a` and `b`, each containing `n` integers (where elements of `a` are in the range 1 to 100 and elements of `b` are in the range 0 to 100). It computes a minimum value based on the ratios of corresponding elements from the lists `b` and `a`, scaled by the elements of `a`, and returns the minimum of these values constrained by `V`. The function does not explicitly handle cases where `b[i]` is zero (which could lead to a division by zero error), nor does it validate that the input adheres to the specified constraints, potentially leading to runtime errors if the input is not as expected.

