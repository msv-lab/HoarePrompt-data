#State of the program right berfore the function call: n and V are integers such that 1 <= n <= 20 and 1 <= V <= 10000. ai and bi are lists of integers with length n such that 1 <= ai[i] <= 100 and 0 <= bi[i] <= 100 for 0 <= i < n.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads input values for `n`, `V`, `ai`, and `bi`, then performs a calculation involving these values. The function does not return any specific value. However, the calculation involves finding the minimum of a complex expression involving the elements of lists `a` and `b`, and then performing further arithmetic operations. It is important to note that the code does not handle any exceptions explicitly, and it is assumed that the input values will always be within the specified constraints.

