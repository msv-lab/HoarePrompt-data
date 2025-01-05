#State of the program right berfore the function call: n is an integer between 1 and 20, V is a positive integer between 1 and 10000, ai is a list of n integers where each integer is between 1 and 100, and bi is a list of n integers where each integer is between 0 and 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts two integers `n` (between 1 and 20) and `V` (a positive integer between 1 and 10000), along with two lists `a` and `b` each containing `n` float values (where `a` values are between 1 and 100 and `b` values are between 0 and 100). It calculates a value by reducing the lists and prints the minimum result computed from the given expressions. However, it does not return any value explicitly, as the function only prints the result. Additionally, the function lacks error handling for input cases that may not conform to the expected ranges or types.

