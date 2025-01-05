#State of the program right berfore the function call: n is an integer in the range 1 to 20, V is an integer in the range 1 to 10000, ai is a list of n integers where each ai is in the range 1 to 100, and bi is a list of n integers where each bi is in the range 0 to 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts two integers `n` (ranging from 1 to 20) and `V` (ranging from 1 to 10000), along with two lists `a` and `b` of size `n` containing floating-point numbers. It calculates a minimum value based on the elements of these lists and prints the result. However, the exact logic of the computation and the intended purpose of the function are not clearly defined in the provided code, and it lacks a return statement, meaning it does not return a value but rather prints it directly.

