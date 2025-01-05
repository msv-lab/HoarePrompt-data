#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 20, V is an integer such that 1 ≤ V ≤ 10000, ai are integers such that 1 ≤ ai ≤ 100 for each i in range(n), and bi are integers such that 0 ≤ bi ≤ 100 for each i in range(n).
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function reads two integers `n` and `V`, followed by two lists of floats `a` and `b`. It calculates a value based on the minimum ratio of elements from `b` to `a`, scaled by each element in `a`, and then returns the minimum of this computed value and `V`. It does not return any value explicitly, but prints the result. The function operates under the constraints that `1 ≤ n ≤ 20`, `1 ≤ V ≤ 10000`, and `1 ≤ ai ≤ 100`, `0 ≤ bi ≤ 100`. The potential edge cases arise from the behavior of the lambda functions and the division operation if any element in `a` is zero.

