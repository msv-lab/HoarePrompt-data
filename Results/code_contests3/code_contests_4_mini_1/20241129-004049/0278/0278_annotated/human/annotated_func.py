#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 20, V is an integer such that 1 ≤ V ≤ 10000, a is a list of n integers where each ai is such that 1 ≤ ai ≤ 100, and b is a list of n integers where each bi is such that 0 ≤ bi ≤ 100.
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 20) and an integer `V` (1 ≤ V ≤ 10000), along with two lists `a` and `b` of size `n` where elements in `a` (1 ≤ ai ≤ 100) and `b` (0 ≤ bi ≤ 100) are provided through standard input. It computes a minimum value based on the provided lists and a specified reduction operation but does not return any value. The function prints the result directly. Additionally, the function does not handle potential input errors or edge cases, such as invalid input types or lengths.

