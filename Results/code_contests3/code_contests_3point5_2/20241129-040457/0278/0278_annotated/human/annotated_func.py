#State of the program right berfore the function call: n and V are positive integers such that 1 <= n <= 20 and 1 <= V <= 10000. ai and bi are positive integers such that 1 <= ai <= 100 and 0 <= bi <= 100.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function `func` reads input values for `n`, `V`, `ai`, and `bi`. It then performs a series of calculations using the input values without explicitly returning any value. The function utilizes `map`, `reduce`, and `zip` functions along with mathematical operations to produce a result that is printed. The code's purpose seems to involve optimization and comparison logic based on the input values, but the exact functionality is complex and not explicitly described. Potential edge cases and missing functionalities may exist due to the intricate nature of the calculations within the code.

