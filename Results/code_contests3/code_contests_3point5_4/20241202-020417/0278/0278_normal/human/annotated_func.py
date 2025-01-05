#State of the program right berfore the function call: n and V are positive integers such that 1 <= n <= 20 and 1 <= V <= 10000. ai and bi are positive integers such that 1 <= ai <= 100 and 0 <= bi <= 100.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads input values for `n`, `V`, `a`, and `b`. It then performs a series of calculations to determine a result based on the given constraints. The function prints the minimum value obtained from the calculations. However, the provided code snippet is incomplete and lacks clarity in terms of the actual calculation process. It utilizes lambda functions, reduce, and zip to perform a complex computation involving the elements of `a` and `b`. The final result is the minimum value obtained from these calculations multiplied by `ai` summed over all elements in `a`, and then compared with `V`. The function does not accept any parameters explicitly, but it relies on the input values provided during its execution. There are potential edge cases related to the input constraints that should be considered to fully understand the functionality of this function.

