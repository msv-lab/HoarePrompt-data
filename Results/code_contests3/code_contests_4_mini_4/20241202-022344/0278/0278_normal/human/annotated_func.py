#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 20, V is an integer such that 1 ≤ V ≤ 10000, ai is a list of n integers where each ai satisfies 1 ≤ ai ≤ 100, and bi is a list of n integers where each bi satisfies 0 ≤ bi ≤ 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads two integers `n` and `V` from input, then reads two lists of floats `a` and `b` of length `n`. It calculates a value based on the minimum of the ratios of elements from lists `b` and `a`, scaled by the elements of list `a`, and then prints the minimum of this calculated value and `V`. If `a` has an element that is zero, this could lead to a division by zero, which is not handled in the code.

