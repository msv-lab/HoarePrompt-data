#State of the program right berfore the function call: n and V are positive integers, ai and bi are positive integers, and all values are within the specified ranges.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function reads two lines of input, calculates the minimum product of pairs of elements from the input lists and multiplies them by the corresponding values in list `a`, then returns the minimum value between the result and `V`. The function does not handle any errors or edge cases related to incorrect input formats or out-of-range values.

