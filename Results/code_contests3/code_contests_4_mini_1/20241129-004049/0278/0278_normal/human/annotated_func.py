#State of the program right berfore the function call: n is a positive integer between 1 and 20, V is a positive integer between 1 and 10000, a is a list of n positive integers each between 1 and 100, and b is a list of n non-negative integers each between 0 and 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts two integers `n` and `V`, followed by two lists of `n` floating-point numbers `a` and `b`. It calculates and prints the minimum value of a specific expression involving the elements of `a` and `b`, subject to the constraint `V`. The function does not handle cases where the input lists may contain zeros or invalid data types, which could potentially lead to errors. Additionally, the function uses `raw_input`, which may not work in Python 3, indicating that it is not compatible with the latest Python versions.

