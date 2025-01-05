#State of the program right berfore the function call: n is an integer between 1 and 20, V is an integer between 1 and 10000, ai is a list of n integers where each integer is between 1 and 100, and bi is a list of n integers where each integer is between 0 and 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts two integers `n` (between 1 and 20) and `V` (between 1 and 10000), along with two lists `a` and `b`, where the elements of `a` are integers (between 1 and 100) and the elements of `b` are floats (between 0 and 100). It calculates a minimum value based on a specified formula involving these parameters and prints this result. However, the function does not handle cases where `b` might contain zero, which could lead to division by zero if such a case arises, potentially causing an error in execution.

