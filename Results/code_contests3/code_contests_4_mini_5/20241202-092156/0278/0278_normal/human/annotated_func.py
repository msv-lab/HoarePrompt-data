#State of the program right berfore the function call: n is an integer between 1 and 20, V is an integer between 1 and 10000, ai is a list of n integers where each element is between 1 and 100, and bi is a list of n integers where each element is between 0 and 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts two integers `n` (between 1 and 20) and `V` (between 1 and 10000), as well as two lists `a` and `b` containing `n` floating-point numbers each. It calculates a minimum value based on the elements of these lists and prints the minimum of the computed value and `V`. The function does not handle any edge cases such as empty input lists or invalid input formats and assumes the inputs will always be provided correctly.

