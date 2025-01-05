#State of the program right berfore the function call: **Precondition**: **n and V are positive integers. ai and bi are positive integers for 1 <= i <= n.**
def func():
    n, V = map(int, raw_input().split())
    a, b = [float(i) for i in raw_input().split()], [float(i) for i in
    raw_input().split()]
    print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab
    [0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))
#Overall this is what the function does:The function reads input values for positive integers n and V, as well as lists of float values for a and b. It then calculates the maximum value of the expression ai + bi * V for each pair of ai and bi, and returns the overall maximum value as an integer. It uses nested reduce and min functions to find the minimum value of ai / bi for each pair, then multiplies it by ai and accumulates the result. The function finally prints the minimum of the accumulated values and V.

